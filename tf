name: Push to Remote Repo

on:
  push:
    branches:
      - main

jobs:
  push_to_remote:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v2

      # Add your steps here to make changes to the repository
      # For example, you can run commands to create or modify files

      - name: Commit changes
        run: |
          git config --local user.email "action@github.com"
          git config --local user.name "GitHub Action"
          git add .
          git commit -m "Auto commit changes"

      - name: Push changes to remote repository
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
          git push https://github.com/${{ github.repository }}.git HEAD:main
