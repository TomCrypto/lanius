# This is *a header* with ***BOLD***

Some **bold** text. This is a fairly long *paragraph* to make sure the text wrapping works [correctly](https://www.somelink.com). It goes on multiple lines just to be sure, blah blah blah... xxxx ok that should be enough.

> Block quote
> Yep

> Another block quote
>
> A list inside a blockquote:
>
> * item1
> * item2
>
> ---
> > another [level][named] of quotes  
> > yep
> ## a sub header inside a block quote??!
>
> and *it keeps going!*

1. Ordered item 1
2. Ordered item 2

* Unordered item 1
* Unordered item 2

Another paragraph, followed by a line break.  
And some more text.

    @lang:c
    int main(void) {
        return 0;
    }

Followed by another normal paragraph with some inline `print('abcdefg')` code.

Some more code:

    @lang:py
    try:
        print("haha")
    except:
        raise ValueError('oops')

---

An unordered list follows:

 * item1, this is a fairly long *paragraph* to make sure the text wrapping works correctly inside list items.
    * _nested item1_
    * nested item2, note this this one has a line break  
    here. And this is the rest of the line.
 * item2

    this is a paragraph continuation of item2

 * another item

An ordered list follows:

 1. item1, this is a fairly long *paragraph* to make sure the text wrapping works correctly inside list items.
 2. item2
    1. nested

        continuation paragraph of nested item, followed by code:

            // i/o example

            #include <iostream>
            using namespace std;

            int main ()
            {
              int i;
              cout << "Please enter an integer value: ";
              cin >> i;
              cout << "The value you entered is " << i;
              cout << " and its double is " << i*2 << ".\n";
              return 0;
            }

        And another paragraph afterwards! With a  
        line break and followed by a blockquote:

        > hi!
        >
        > ## some **section**
        >
        >     @lang:c
        >     int main() {
        >         return 0;
        >     }

    2. nested2 **bold**

---

Some ***bold AND italics*** text.

**bold**

## Another subheader

### Subheader 3

#### Subheader 4

##### Subheader 5

###### Subheader 6

> Another blockquote

Now we write some links. First an [inline link](http://www.google.com) here.

[named]: http://example.com/
