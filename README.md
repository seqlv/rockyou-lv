# Latvian rockyou.txt database

This project has been created for educational purposes.
The project aims to educate society on how quickly easily passwords can be brute-forced if they lack complexity.

## Methodology

We collected combo lists that are available on (semi-)clear web, modified them according to the basic `e-mail/username:plaintext password` structure, and used `rockit.py` to do the rest. Passwords are filtered based on TLD `.lv`. The output contains only those passwords that have been used at least twice — minimizing the risk of exposing personally identifiable information.

## Statistics for 2024-02-18

| Statistic | Value |
| --- | --- |
| Total lines processed | 165684182 |
| Total data processed (MB) | 5177.18 |
| Previous .lv TLD count | 440389 |
| New .lv TLD count | 170202 |
| Difference in .lv TLD count | -270187 |
| Previous rockyou-lv count | 38662 |
| New rockyou-lv count | 15287 |
| Difference in rockyou-lv count | -23375 |
| Processing time (seconds) | 63.42 |

### Top 10 .lv TLD Email Providers

| Rank | Provider | Occurrences |
| --- | --- | --- |
| 1 | inbox.lv | 128642 |
| 2 | one.lv | 12066 |
| 3 | tvnet.lv | 4984 |
| 4 | apollo.lv | 2305 |
| 5 | navigator.lv | 1132 |
| 6 | e-apollo.lv | 1100 |
| 7 | delfi.lv | 1063 |
| 8 | balticom.lv | 494 |
| 9 | latnet.lv | 477 |
| 10 | lu.lv | 272 |

## Contributing

If you wish to contribute by improving the code, just create a pull request.

If you think you have data that would be beneficial to the list, let us know.

## Credits

[www.seq.lv](https://www.seq.lv/) - [root@seq.lv](mailto:root@seq.lv)

Nils Putnins, OSCP — [np@seq.lv](mailto:np@seq.lv)