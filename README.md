# Placeholder Docker
This container provides a placeholder for integration purposes during further development of our PET/CT algorithm. When running this container, it outputs a random tumor malignancy score between 0-1.

## Run with included test data
When running without arguments, the docker loads two packaged mha-files and a virtual coordinate stored in json. It outputs a random tumor malignancy score.

```shell
docker run philips_placeholder
```


## Run with custom test data
It is also possible to run the test with another set of a CT-scan, PET-scan, and a coordinate.

Be sure to have the following image structure.
```
/root/
    /images/
        ct_scan.mha
        pet_scan.mha
        coordinates.json
```
The images can be any mha-files of a CT-scan or PET-scan. The structure of the json-file should look like this:
```json
{
    "x": 0,
    "y": 0,
    "z": 0
}
```

Run the following command **from the root folder**. 
```shell
docker run -v $(pwd)/images:/images/ philips_placeholder python app.py [ct-file-name] [pet-file-name] [coordinates-file-name]
```

So according to the example:
```shell
docker run -v "$(pwd)/images:/images/" philips_placeholder python app.py ct_scan.mha pet_scan.mha coordinates.json
```