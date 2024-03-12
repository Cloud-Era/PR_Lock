- name: Checkout repository
        uses: actions/checkout@v2  # Action to checkout the repository

      - name: Print current directory
        run: pwd  # Command to print current directory

      - name: List all files and directories
        run: ls -a  # Command to list all files and directories, including hidden ones
