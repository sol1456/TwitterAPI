# coding: utf-8

class PATH:

  HOST    = 'https://api.twitter.com/1.1';


  USER       =  HOST + '/users/show.json';

  FOLLOWERS  =  HOST + '/followers/ids.json';

  TWEET      =  HOST + '/statuses/update.json';


  ID_BLOCKED =  HOST + '/blocks/ids.json';

  U_BLOCKED  =  HOST + '/blocks/list.json';


  FOLLOW     =  HOST + '/friendships/create.json';

  REMOVE     =  HOST + '/friendships/destroy.json';



  SETTINGS   =  HOST + '/account/settings.json';

  PROFILE    =  HOST + '/account/update_profile.json';

  IMAGE      =  HOST + '/account/update_profile_image.json';

  U_BANNER   =  HOST + '/account/update_profile_banner.json';

  R_BANNER   =  HOST + '/account/remove_profile_banner.json';