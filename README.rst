Class for use https://developers.google.com/youtube/v3/docs/

.. image:: https://badge.fury.io/py/googleapis_youtube.svg
    :target: https://badge.fury.io/py/googleapis_youtube


=======
Install
=======

.. code-block:: bash

    pip install googleapis_youtube

=======
Example
=======

.. code-block:: python

    from googleapis_youtube.api import YoutubeAPI

    YOUTUBE_API = 'api key'
    CHANNEL_NAME = 'id channel'
    result = YoutubeAPI(YOUTUBE_API)
    videos = result.videos_channel(CHANNEL_NAME)


=======
Donation
=======

.. image:: https://img.shields.io/badge/Donate-PayPal-green.svg
  :target: https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=YYZQ6ZRZ3EW5C
