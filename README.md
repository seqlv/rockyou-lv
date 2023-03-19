# Latvian rockyou.txt database

This project has been created for educational purposes.
The project aims to educate society on how quickly easily passwords can be brute-forced if they lack complexity.

## Methodology

We collected combo lists that are available on (semi-)clear web, modified them according to the basic `e-mail/username:plaintext password` structure, and used `rockit.py` to do the rest. Passwords are filtered based on TLD `.lv`. The output contains only those passwords that have been used at least twice — minimizing the risk of exposing personally identifiable information.

## Contributing

If you wish to contribute by improving the code, just create a pull request.
If you think you have data that would be beneficial to the list, let us know.

## Credits

[www.seq.lv](https://www.seq.lv/) - [root@seq.lv](mailto:root@seq.lv)
Nils Putnins, OSCP — [np@seq.lv](mailto:np@seq.lv)