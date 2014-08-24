# Simple backup script using [Bakthat](https://github.com/tsileo/bakthat)

Before run this script you should install and configure Bakthat as follows:
```
$ pip install bakthat sh
$ bakthat configure
```

Also, if you're using MySQL:

```
$ mysql_config_editor set --login-path=local --host=localhost --user=localuser --password
```

To better understand the GFS backup rotation I recommend you to check this video: [https://www.youtube.com/watch?v=7oNlwQ46XS4](https://www.youtube.com/watch?v=7oNlwQ46XS4). In addition, there's a sample configuration file named .bakthat.yml.

# License (MIT)

Copyright (c) 2014 Igor de Lorenzi Andrade

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.