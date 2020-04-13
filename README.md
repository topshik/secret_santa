# Secret Santa
People like presents and also like Christmas game Secret Santa, where you can recieve gifts from unknown people. This script allows you to host a Secret Santa game, so that no one including an organizing person knows each others' santa :)

The script needs a .csv table which contains data in the form `name, email, place for gift recieving, wishlist, alletgies`. You can easily collect such data via google form. Table needs to be without headers, otherwise you need to modify `pd.read_csv()` default parameters. You can find example of a table in `data_example.csv`.

## Usage
1. First of all, collect data as described above and place it into the the file `data.csv`
2. Secondly, edit the script file, entering your email, password and a letter subject as a python string into correspondig variables.
3. Then you need to allow usage of external apps in your [https://support.google.com/accounts/answer/6010255](account settings)
4. Finally, run script and enjoy your Christmas gifts :)
