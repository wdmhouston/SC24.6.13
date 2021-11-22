.. _AccessApi:

###############################
Access API
###############################

The following apis are supported in current release. 

prediction
==============================
To predict, an image should be copied to upload folder in project folder, and the image name is appended to /api/predict/ in url.

For example, to predict the fruit type from an image with name "apple_1.jpg" in upload folder(172.17.0.2 is the ip of the running docker image, replace it with the real ip in your case):

.. code-block:: sh

  $ curl http://172.17.0.2:5000/api/predict/apple_1.jpg
	{
		"code": 0,
		"data": {
			"image": "/app/project/upload/apple_1.jpg",
			"result": "apple"
		},
		"message": "ok"
	}
	
If image path is wrong:

.. code-block:: sh

  $ curl http://172.17.0.2:5000/api/predict/apple_3.jpg
	{
		"code": 1,
		"data": {},
		"message": "fail to read image"
	}
	

Below is a list of attributes returned by api/predict

+---------+---------------------------------------------------------+
| name    | note                                                    |
+=========+=========================================================+
| code    | 0: success, 1: fail                                     |
+---------+---------------------------------------------------------+
| nessage | ok or reason of fail                                    |
+---------+---------------------------------------------------------+
| data    | image path and prediction result will be returned       |
+---------+---------------------------------------------------------+

zz
