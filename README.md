
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

Here's a minimal command to run the container:

```
docker run --rm -it --detach-keys ctrl-z,z --name emacs-py emacs-py
```

Add to the above options to:

- map a directory on the host where the projects are onto the container;

- open ports for web servers in the container that I want to access with the browser on the host:

```
docker run --rm -it --detach-keys ctrl-z,z --name emacs-py \
-v $(pwd)/Documents/code:/code \
-p 8080:8080 \
emacs-py
```

### use with Python:

- Create a virtual environment for your project. Install pyright and jsonrpc.

- On Emacs:
  - `M-x venv-workon` to activate the virtual environment, then
  - `M-x eglot`

Reference:
https://olddeuteronomy.github.io/post/python-programming-in-emacs/

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

### copy text out of Emacs onto the host's clipboard:

Save it to a file, let's say `clipping`. If the host is a Mac, do `pbcopy < clipping`. If it is Linux, `xsel -b < clipping`.
