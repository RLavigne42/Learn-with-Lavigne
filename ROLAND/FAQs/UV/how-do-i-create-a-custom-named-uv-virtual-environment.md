## How do I create a custom-named uv virtual environment?

You can create a uv-managed virtual environment in a folder name you choose (instead of the default `.venv`). The basic workflow is: go to your project directory, optionally remove an old environment, create the new one with your custom name, activate it, then install dependencies.

1. **Navigate to your project folder**  
   In your terminal, change into your project directory:

   ```bash
   cd /path/to/your/project
   ```

2. **(Optional) Remove an old environment if you’re resetting**  
   If an environment is already active, deactivate it first, then delete the old environment folder:

   ```bash
   deactivate
   rm -rf <env_name>
   ```

3. **Create the custom-named virtual environment**  
   Replace `<env_name>` with the folder name you want for the environment:

   ```bash
   uv venv <env_name>
   ```

4. **Activate the environment**  
   Activate using the folder name you chose:

   ```bash
   source <env_name>/bin/activate
   ```

   Your terminal prompt will typically change to show the environment name.

5. **Install dependencies (example using `requirements.in`)**  
   If your project uses a `requirements.in` file, compile and sync dependencies like this:

   ```bash
   uv pip compile requirements.in -o requirements.txt
   uv pip sync requirements.txt
   ```
