import os

# Determine the current operating system
if os.name == 'nt':  # Windows
    platform = 'windows'
elif os.name == 'posix':  # Linux/Unix/MacOS
    platform = 'linux'
else:
    raise NotImplementedError(f"OS {os.name} not supported")

if platform == 'windows':
    import win32clipboard as clipboard

    def copy_to_clipboard(html_content: str):
        try: 
            # Register the HTML format with Windows
            cf_html = clipboard.RegisterClipboardFormat("HTML Format")

            # Construct the HTML clipboard content
            header = """
                Version:0.9
                StartHTML:00000097
                EndHTML:{1:09d}
                StartFragment:00000133
                EndFragment:{0:09d}
                <html><body><!--StartFragment-->{2}<!--EndFragment--></body></html>
                """
            html = header.format(len(header) + len(html_content) + 1, len(header), html_content)

            # Open the clipboard
            clipboard.OpenClipboard()

            # Empty the clipboard
            clipboard.EmptyClipboard()

            # Set clipboard data for the registered HTML format
            clipboard.SetClipboardData(cf_html, html.encode("UTF-8"))
        except Exception as e:
            raise ValueError("Could not set clipboard data {e}")
        
        else:
            return "Copied to clipboard"

        finally:
            # Close the clipboard
            clipboard.CloseClipboard()
        
elif platform == 'linux':
    import subprocess

    def copy_to_clipboard(html_content:str):
        try:
            subprocess.run(['xclip', '-selection', 'clipboard', '-t', 'text/html'], input=html_content, text=True, check=True)
            return "Copied to clipboard"
        except subprocess.CalledProcessError:
            # Fallback or error handling
            raise RuntimeError("Could not copy to the clipboard. Ensure xclip is installed.")
