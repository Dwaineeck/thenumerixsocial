import json
import os
import time

import nbformat
from gtts import gTTS
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer


def extract_content(file_path):
    """
    Extracts titles and their corresponding content from a Jupyter Notebook, including both top-level and second-level headers.

    Args:
    file_path (str): The path to the Jupyter Notebook file.

    Returns:
    list: A list of tuples, each containing the title and corresponding content.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            nb_content = nbformat.read(f, as_version=4)

        sections = []
        current_title = None
        current_content = []

        for cell in nb_content.cells:
            if cell.cell_type == 'markdown':
                for line in cell['source'].split('\n'):
                    # Check for headers
                    if (line.startswith('# ') or line.startswith('## ')) and line[2:].strip():
                        if current_title:
                            sections.append(
                                (current_title, '\n'.join(current_content)))
                        current_title = line.strip()  # Keep the leading # or ##
                        current_content = [line.lstrip('#').strip()]
                    elif current_title:
                        current_content.append(line)
            elif cell.cell_type == 'code' and current_title:
                current_content.append(cell['source'])

        if current_title:
            sections.append((current_title, '\n'.join(current_content)))

        return sections

    except FileNotFoundError:
        print(f'File not found: {file_path}')
        return []
    except PermissionError:
        print(f'Permission denied: {file_path}. Please check file permissions.')
        return []
    except Exception as e:
        print(f'Error extracting content from {file_path}: {str(e)}')
        return []



def text_to_speech(text, output_file):
    """
    Converts text to speech and saves it as an MP3 file.

    Args:
    text (str): The text to convert to speech.
    output_file (str): The path to save the audio file.
    """
    tts = gTTS(text=text, lang='en')
    tts.save(output_file)
    print(f'Audio content written to {output_file}')


def process_sections(sections):
    """
    Processes extracted sections (e.g., creates audio files).

    Args:
    sections (list): List of tuples containing (title, content) extracted from a notebook.
    """
    try:
        if not os.path.exists('audio'):
            os.makedirs('audio')

        for index, (title, content) in enumerate(sections, start=1):
            sanitized_title = title.replace(" ", "_").replace(
                "#", "").replace("/", "_").strip()
            first_word = sanitized_title.split('_')[0]
            folder_path = os.path.join('audio', first_word)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            audio_file = os.path.join(folder_path, f'{index:02d}_{sanitized_title}.mp3')
            text_to_speech(content, audio_file)

        with open('sections.json', 'w') as f:
            json.dump(sections, f)
        print('Sections and audio files created.')
    except Exception as e:
        print(f'Error processing sections: {str(e)}')


class NotebookHandler(FileSystemEventHandler):
    def __init__(self):
        super().__init__()

    def on_created(self, event):
        if event.is_directory or not event.src_path.endswith('.ipynb'):
            return
        print(f'New notebook file created: {event.src_path}')
        sections = extract_content(event.src_path)
        if sections:
            process_sections(sections)
        # Move or delete the processed notebook file as needed
        # os.remove(event.src_path)  # Uncomment if files need to be removed after processing


def monitor_courselist(directory):
    """
    Monitors the 'courselist' directory and its subdirectories for new Jupyter Notebook files (.ipynb).
    When a new file is added, extracts its content and creates audio files.

    Args:
    directory (str): Path to the 'courselist' directory.
    """
    try:
        print(f"Monitoring directory and subdirectories for new notebooks: {directory}")
        event_handler = NotebookHandler()
        observer = Observer()
        observer.schedule(event_handler, directory, recursive=True)
        observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
            observer.join()
    except Exception as e:
        print(f'Error in monitor_courselist: {str(e)}')


if __name__ == "__main__":
    courselist_dir = 'courselist'
    monitor_courselist(courselist_dir)
