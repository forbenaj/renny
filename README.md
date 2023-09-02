# 🤖 Renny - Just a little guy inside your computer

Renny is a little person who lives in your computer. He likes to wander through your directories, browse your files, give his opinion on your texts, and write in his journal all his adventures. He's essentially a bening virus. At the end of the day, Renny returns to his little house, which is nothing more than a folder on the desktop where he keeps his stuff (shortcuts to his favorite folders, his travel-journal.txt, photos of his adventures, etc).

From time to time it is possible to find Renny browsing through our folders. If we double click on him, we can talk to him, and he will tell us what he is doing. It is also possible to use our "communicator", which is a small program to talk to him wherever he is. If he wants, he will tell us where he is and if we can visit him.

Only tested on Windows because I'm not a nerd. Would love some help from nerds to make it work on Linux.


## Features

- **He just walks around:** ¯\_(ツ)_/¯ He just walks around
- **Interactive Conversations:** Chat to Renny to engage in conversations with him and discover what he's up to.
- **Customizable personality:** By modifying the "definition" in the associated character in Character.AI 

## Technology

Renny is built using Python and leverages the Character.AI API, which communicates with a specific character trained to talk back with JSON strings, so his responses can be directly handled by the script.

## Installation

To bring Renny to life in your computer, follow these simple steps:

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/forbenaj/renny.git
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the main program to release Renny:

   ```bash
   python main.py
   ```

## Getting Started

You'll need a Character.AI account token to use the API.

- **Get your token:**
1. Create a Character.AI account
2. On the main page, open the DevTools (F12)
3. Go to Application tab, and look for Local Storage > https://beta.character.ai/
4. Copy the value from the key "char_token"

DO NOT SHARE YOUR TOKEN, IT GIVES ACCESS TO YOUR ACCOUNT

- **Release Renny:**
1. Paste your token in the Token field
2. Leave the suggested character ID or write your own (Instructions below)
3. Release Renny!

Once you've released Renny, he'll start traveling through your folders and checking files.

Every few minutes, the background script will make a request to the associated character, sending the current state Renny needs to know where he's at. Renny will respond with a JSON string with two values: what's on his mind, and what he'll do next.

- **Good practices:**
I'm pretty sure characters learn from everybody, so if you use a shared ID like mine, Renny's personality may be influenced by many users. I don't know to what extent, or if votes are required for it to work.
For most purposes, you can use my Renny's character ID, with a few considerations that you should also apply to your own character:

- Do not talk directly to him through the Character AI webpage chat. Let him be trained with the severity of the script only.
- If renny commits a mistake, generate a new response through the Character AI webpage chat, until it responds something sane.
- Just don't try to make him a criminal.

You can experiment by creating your own character. I'd love to see experiments on other definitions, greetings or descriptions.
  
- **Creating your own Renny:**
  1. In the Character AI webpage, go to Create and select Create a Character
  2. Click on Edit Details (Advanced)
  3. Name him whatever you want
  4. Copy all values from the definition.txt file, including Greeting, Short Description, Long Description and Definition
  5. Save your character, and copy the char value from the URL

## Usage

¯\_(ツ)_/¯ He just walks around.

- Talk to him if you want, or open the console to spy on him.
- Get his opinions on your texts.
- Catch him nosing around in things he shouldn't!

## Contributing

I welcome contributions from the community to enhance Renny's capabilities and make him an even more delightful companion. If you'd like to contribute, please:

1. Fork this repository.
2. Create a new branch for your feature or bug fix: `git checkout -b feature/your-feature`.
3. Make your changes and commit them: `git commit -m "Add your feature"`.
4. Push to your forked repository: `git push origin feature/your-feature`.
5. Open a pull request, and I'll review your contribution.

Also, please create Renny characters in the Character AI website and experiment with them!

I hope Renny enjoys having a vacation in your computer!

![Renny](renny.png)
