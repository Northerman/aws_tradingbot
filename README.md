# AWS Trading Bot using Alpaca API: Project Overview
* Trading bot deployed on AWS utilizing ECR (Elastic Container Registry) to deploy a docker image.
* Trade Strategy: RSI (Relative Strength Index) overbought/oversold.
* Utilize AWS EventBridge to execute trade strategy when market open
* Amazon SNS to Send SMS to phone tracking daily portfolio change.
* Amazon RDS to store data of trade positions into the database for further analytics.
* (Possible to do) Connect Analytics tool like tableau for analysis.
![](/trade_bot.jpg)
# Code and Resources Used
* Available in DockerFile

