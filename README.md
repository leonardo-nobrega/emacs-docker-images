
# Emacs docker images

Docker images for software development, containing Emacs and one or more of the following languages:

- Python

## Why?

- To have a piece of code that lists everything I use to work on programs.

- To have a work environment that I can use on any machine running docker.

- To avoid as much as possible installing packages I will forget about on my machines.

## How to...

### build the image:

```sh
# create a dockerfile from the template using render.py
source venv/bin/activate
python render.py -l py

# build the image
docker build -t emacs-py .
```

### run a container after building an image:

```
docker run --rm -it --detach-keys ctrl-z,z --name emacs-py emacs-py
```

### develop:

- Make a change to the template, the `render.py` program or one of the test suites: `build_test.py` and `run_test.py`.

- Render a dockerfile to build the test image; pass the `-t` option to the render program. Optionally, pass the `-f` option to skip the overwrite question.

  The dockerfile will have code to install all languages.

  ```
  python render.py -t
  ```

- Build the test image.

  ```
  docker build -t emacs-py-test .
  ```

- Run a container with the test image.

  ```
  docker run --rm emacs-py-test
  ```
