# TwitterAPI

## Description

	
	Python2.7.1.3

	This repository uses OAuth authentication of 
	Twitter API with requests_oauthlib

	Install the package with pip

	>>> pip install requests_oauthlib

	



## function description


	tweet()
		- text contents tweeted


	updateProfile()
		* Parameters

			- string name : account display name
			- string url  : website url
			- string location    : residence
			- string description : self introduction text
			- string profile_link_color : Theme color

			- bool skip_status : Whether to exclude the return value JSON's status property in the user object
			- bool include_entities : Whether to include the entities property of the return value of JSON in the tweet object


	updateSetings()
		* Parameters

			- string lang : region
			- string time_zone : time zone

			- bool sleep_time_enabled : Whether sleep setting is enabled or not

			- int end_sleep_time : Sleep end time is specified by 2 digit time (00 ~ 23)
			- int start_sleep_time : Sleep start time is specified by two digit time (00 ~ 23)
			- int trend_location_woeid : The target area of ​​the trend. It is specified by WOEID


	updateProfileImage()
		- Update profile image


	updateProfileBanner()
		- Update profile banner image


	removeProfileBanner()
		- Remove profile banner image




	getSettings()
		- Get setting contents


	getBlockedUserIds()
		* Parameters

			- int cursor : Specify the cursor indicating the acquisition start position

			- bool stringify_ids : Whether to accept the value as a character string



	getBlockedUserList()
		* Parameters

			- int cursor : Specify the cursor indicating the acquisition start position

			- bool skip_status : Whether to exclude the status property in the user object
			- bool include_entities : Whether to include entities property in tweet object


	getUserByScreenName()
		- Get user information by screen name