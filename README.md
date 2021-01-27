# webots-competition-organizer

[![Webots Badge](https://badgen.net/badge/icon/Rankings?label=Webots)](https://cyberbotics.github.io/webots-competition-organizer-template/)

## Organize

### Make repositories
First, you need to make a repository like this by clicking on the green button `Use this template`.
You also need to do the same for [the competitor repository](https://github.com/cyberbotics/webots-competition-competitor-template) so the competitors can fork it and push their controllers.

### Personal Access Token

PAT (Personal Access Token) is necessary to be able to pull a code from a participant's private repositories.

- Generate a new token [here](https://github.com/settings/tokens). In the `Select scopes` section check `repo`.
  - If this repository is hosted at a GitHub organization you will need to create a new GitHub account and generate the token for it.
- [Create a new secret](https://docs.github.com/en/free-pro-team@latest/actions/reference/encrypted-secrets#creating-encrypted-secrets-for-a-repository), name it `BOT_PAT_KEY` and paste the key you have just generated.
- [Create a new secret again](https://docs.github.com/en/free-pro-team@latest/actions/reference/encrypted-secrets#creating-encrypted-secrets-for-a-repository), name it `BOT_USERNAME` and put your username in it.
  - If this repository is hosted at a GitHub organization use your bot's username.
- Let the participants know they have to add your username to `Settings > Manage access` so you have the right to clone their private repositories.

### Customize
The sample competition is just a sample and you probably want implement a custom scenario and rules.

- Change the scenario in the world file ([`worlds/competition.wbt`](worlds/competition.wbt)).
- Change the [`contest manager controller`](controllers/contest_manager):
  - The purpose of this [supervisor](https://www.cyberbotics.com/doc/reference/supervisor) controller is to keep a track of the competitors and their points, something like a referee.
  - You should write the competition results to `/tmp/results.txt`, so the results can be parsed by CI.
    ```bash
    # Format of `/tmp/results.txt`:
    #   winner: [index of winner]
    #   points: [points of the first robot], [points of the second robot]
    winner: 0
    points: 111, 0
    ```
  - Once the match is over, you should use the [Emitter](https://www.cyberbotics.com/doc/reference/emitter) node to send `done` on channel 1024 so our animation recorder is aware the match is done.

## Publish the results
The Webots GitHub action generates a preview of the competition and publishes it to the `gh-pages` branch.
Therefore, you have to choose the `gh-pages` branch [as the publishing source](https://docs.github.com/en/free-pro-team@latest/github/working-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site#choosing-a-publishing-source).
Then, you can access the preview at `[your_username].github.io/[your_repo_name]`.
