## How do I run a Python application inside a uv virtual environment?

To run a Python app in a uv virtual environment, you first activate the environment so your `python` and installed packages come from that environment. Then you run your project’s scripts normally with `python <script>.py`. If your project has multiple scripts, run them in the order your workflow requires.

1. **Activate your uv virtual environment**  
   From your project folder, activate the environment (replace `<env_name>` with your environment folder name):

   ```bash
   source <env_name>/bin/activate
   ```

   Your terminal prompt will typically change to indicate the environment is active.

2. **Run your Python script(s)**  
   Run the main script(s) using Python:

   ```bash
   python run_app.py
   ```

   If you have a second step (for example, an assembler/build script), run it next:

   ```bash
   python assemble_output.py
   ```

3. **Check the output files**  
   Any generated logs or output files will be created in the locations defined by your scripts (often the current project folder). If you don’t see expected output, confirm you’re in the correct directory and that the environment is still activated.
