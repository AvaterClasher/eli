## Eli - Your AI-powered Personal Coding Assistant

> :warning: - You need a OpenAI auth token to make Eli work. You can find more here [OpenAI](https://openai.com/pricing)

> :package: - Check out <a href="https://pypi.org/project/eli-pa">Eli on PyPI (PIP) </a>

Eli is a CLI-based Personal AI assistant that is powered by the GPT-3 / GPT-4 versions supported by [MindsDB](https://mindsdb.com).

### Installation

Make sure you have `pip` and `python >= 3.6` installed on your machine and follow the steps.

<details>
    <summary><h4>1. Setup the package</h4></summary>

##### Option A - Download from PyPI archive

```sh
pip install -U eli-pa
```

##### Option B - Download from GitHub archive

```sh
pip install git+http://github.com/AvaterClasher/eli.git
```

> :warning:: Eli is POSIX-friendly. For it to properly work on Windows please run Eli through a Wsl instance.

</details>

<details>
  <summary><h4>2. Set the <code>MINDSDB_EMAIL_ADDRESS</code> environment variable</h4></summary>

Once you got the package installed on your system, it's time to add the `MINDSDB_EMAIL_ADDRESS` environment variable. Create an account on [mindsdb.com](https://mindsdb.com/), train your GPT model and replace your email with `<EMAIL>` in the following options.

##### > If you use the default bash shell

```sh
echo "export MINDSDB_EMAIL_ADDRESS=<EMAIL>" >> ~/.bashrc
```

##### > If you use ZSH

```sh
echo "export MINDSDB_EMAIL_ADDRESS=<EMAIL>" >> ~/.zshrc
```

> :bulb:: Read the article for more information about training your MindsDB model.

</details>

<details>
  <summary><h4>3. Set your MindsDB account password</h4></summary>

Now, it's time to set your account's password. Simply run `eli` with the `--auth` option and enter your MindsDB account password.

```sh
eli --auth
```

You're all set to go. :)

</details>

### Usage

Use `eli` followed by your question and it'll process the phrase and responses back the content in Markdown.

```
$ eli where is london located

London is the capital city of the United Kingdom and is located in the southeastern part of England, in the region known as Greater London.
It is situated along the River Thames and is one of the most populous and culturally significant cities in the world.
```

```
$ eli tell me a programming joke

Why do programmers prefer iOS development over Android development?
Because on iOS, you only have to deal with one "byte."
```

```
$ eli add annotations to this file: $(cat file.py)

To add annotations to the given Python function, you can include comments and
docstrings to provide more information about the function's purpose and usage.
Here's an example:

    def factorial(n):
    """
    Calculate the factorial of a non-negative integer.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    return 1 if n == 0 else n * factorial(n - 1)

# Example usage:
number = 5
result = factorial(number)
print(f"The factorial of {number} is {result}")

```

### Tech Stack

-   Tools
    -   [Python](https://python.org)
-   Infrastructures & Hosting
    -   [MindsDB](https://mindsdb.com)
    -   [PyPI](https://pypi.org)

### License

Eli is being licensed under the [MIT License](https://github.com/AvaterClasher/eli/blob/main/LICENSE).
