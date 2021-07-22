# AWS Trading Bot using Alpaca API: A Starter code for trading bot
* Trading bot deployed on AWS utilizing ECR (Elastic Container Registry) to deploy a docker image.
* Trade Strategy: RSI (Relative Strength Index) overbought/oversold.
* Utilize AWS EventBridge to execute trade strategy when market open
* Use Amazon SNS to Send SMS to phone tracking daily portfolio change.
* Store data using Amazon RDS logging trade positions into the database for further analytics.
* Connect Analytics tool like tableau for analysis.
![](/trade_bot.jpg)
![](/SNS.jpg)
# Code and Resources Used
* Big thanks to McKlayne Marshall guide available in his Medium: https://mcklayne.medium.com/
* Requirements: Available in DockerFile

