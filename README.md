# Prototype of a quiz application

The back-end is a Flask based Python application.

## Using

A `Makefile` is provided with common tasks. Note the `.venv` target for setting up.

### Running/Building

`make serve` runs the flask application in port `8000`. It watches the `src/server`, `src/templates` and `dist` folders.

### Testing

`make test` runs the tests

`make debug` runs the tests.

### Linting

`make lint` runs the linters.

# Deployment

The application is deployed automatically on each commit, using GitLab CI, to a Heroku instance. It runs [here](#TODO).
