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
    import win32con

    def copy_to_clipboard(html_content:str):
        # Open the clipboard
        clipboard.OpenClipboard()

        # Empty the clipboard
        clipboard.EmptyClipboard()

        # Set the clipboard data as HTML format
        # Windows requires a specific format for HTML to be recognized by applications.
        # This includes a header with version, start HTML, end HTML, start fragment, and end fragment positions.
        header = "Version:0.9\r\nStartHTML:00000097\r\nEndHTML:{1:09d}\r\nStartFragment:00000133\r\nEndFragment:{0:09d}\r\n"
        markup = "<html><body><!--StartFragment-->{0}<!--EndFragment--></body></html>".format(html_content)
        payload = header + markup
        payload = payload.format(len(payload) + 1, len(header))
        
        # Set clipboard data
        clipboard.SetClipboardData(win32con.CF_HTML, payload.encode("UTF-8"))

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
