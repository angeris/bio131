# Introduction to Topology

## Intro

Pardon the long-ish post. This is a set up for the next post coming up on Iterated Fractal Systems (which is actually a really beautiful topic that I'd like to present the math behind without being terribly ridiculous), with a bunch of fancy-schmancy images. But, anyways, let's get down to business.

## What *is* topology?

*Topology* is what happens when we strip all sensible ideas from geometry and stick with only the completely insensible ones: mainly the notion of open sets. I guess the first question that would come to most sane people is... *why is this useful at all?* 

I mean, seriously, someone actually said something along the lines of: let's take geometry and everything that makes it, well, geometry, and just drop it entirely. Because we can and because this is math, so why the hell not?

Anyways, back to the question: open sets. Open sets are useful because if you picture stretching, contracting, or otherwise messing with a fabric (without ripping it! Or making a hole in it... more on that in a bit), you should note that any open set is somehow preserved, that is, it remains open, even though it's been stretched/rotated or whatever.

![I mean, if you make a hole in it, I guess it's technically "more open" (as in, I have a box and I opened it) but bear with me, this is math.](http://imgur.com/LIRtAAY.png "Open sets")

### Metric Spaces

Okay, fine. Let's now put that in more formal terms:

We have some set $X$ that represents the space (this can be anything you like, really. For example, $X$ can be the set of all real numbers [$\mathbb{R}$], or the set of vectors in 2 dimensions [$\mathbb{R}^2$], or the set of functions that are square-integrable [$L^2$][^lp2]) with some distance measure $d(x,y)$ (in the real numbers, the distance between two numbers can be, say, the absolute difference between them, and in $\mathbb{R}^2$ it can be the usual distance between vectors).

We want the distance function $d$ (written in fancy math form as $d: X\times X \to \mathbb{R}^+_0$, read as "$d$ is the function that maps two elements of the set $X$ into the positive real numbers").

1. We want it to be always non-negative (as negative distances don't really make any sense), that is 
    $$d(x,y) \ge 0$$
2.  We want the distance to be symmetric (the distance between you and me should be the same as the distance between me and you)
    $$d(x,y) = d(y,x)$$
3. We want the distance to be non-degenerate. That is, if the distance between two points $x,y$ is zero, that means that they should be *the same point*, that is 
    $$d(x,y) = 0 \iff x=y$$
4. And we want the distance to satisfy the triangle inequality: the distance between two points $x\to y$ should be at most as great as the distance through a third, say $x\to z\to y$. More formally:
    $$d(x,y) \le d(x,z) + d(z,y)$$

![Not the most exciting of things, but it's damn useful.](http://imgur.com/NuV0AIF.png "Triangle Inequality")

Those four properties together tell us that $d$ is, indeed, a distance function! Surprisingly, this is all we really need to do a lot of cool stuff.

### Neighbourhoods and Open Sets

Now, let's start getting to the punchline. I'm going to throw out two quick definition that shouldn't be taken too seriously---the notion of an open ball and the notion of a *neighbourhood* of a point. In particular, these are almost exactly what they sound like: an open ball is one that doesn't contain its boundary, and a neighbourhood is a set that *surrounds* a point.

An open ball of radius $r>0$ centered at $x$ is defined as the set:
$$
B_r(x) \equiv \{y \,|\, d(x,y) < r\}
$$
that is, the set of all points that are less than a distance $r$ away from $x$ (think of an [open] circle in 2 dimensions; it is the set of all points that are less than a distance $r$ away from the origin).

![It's a lot of colors, but it mostly makes sense, I promise.](http://imgur.com/dIZVrVy.png "Open Ball")

We then define neighbourhood based on the definition of an open ball! We say $N$ is a neighbourhood of $x$ when there is some open ball surrounding $x$ completely contained in $N$. In math-y terms, there exists some $r>0$ such that
$$
B_r(x)\subset N
$$
where $A\subset B$ means that the set $B$ completely contains the set $A$.

And, finally, we say a set $S$ is *open* if $S$ is a neighbourhood of all of its points.[^openness]

## Completeness, Banach, and Fixed Points

### Limits and Completeness

Limits! And you thought you'd be done with them after calculus... Anyways, they reemerge in topology as an extremely useful tool to analyze continuity (though we won't do that here) among other things. In our case, it will allow us to state the existence of IFS, but in the meantime, we show a few things before that:

We say a space $X$ with a metric $d$ is complete if it contains all of its limit points. A limit point, is, intuitively, the limit of some sequence that gets arbitrarily close to a point; in other words, we say the sequence $\{a_n\}$ tends to the point $a$ when, once we go far along enough in the sequence, $\{a_n\}$ gets arbitrarily close to $a$. In terms of neighbourhoods (as previously defined), we have that $a$ is a limit point of $\{a_n\}$ if, for any neighbourhood $M$ around $a$ we have $a_n\in M$ for all $n>N$.

Intuitively this means that, if I give you some neighbourhood $M$ of the limit point, you can always give me some number $N$ such that the sequence, after the $N$-th term, is always inside of the neighbourhood.

This is all we need to get to proving actually useful theorems.

### Fixed Points

Consider some function $T$ which shrinks the space[^contraction]---that is, it brings any two points in the space closer together. Mathematically, that means, for any two points $x, y$ in our space $X$, we have
$$
d(T(x),T(y)) \le qd(x,y) 
$$
where $0\le q < 1$ is the fraction by which we shrink our space (note that it must necessarily be less than one, otherwise we could allow our space to remain the same and never bring any two points closer together). I won't quite prove *existence* of a limit point[^cauchy], but I will make a quick argument for it:

Consider any point $x$ in the space. We know that $T$ shrinks the *entire* space, hence why don't we apply it repeatedly on $x$? Right? Since we bring any two points closer together, applying $T$ infinitely many times should bring every point in the space infinitely close to each other! That is, they are all the same point. Let's see how this plays out. Take the sequence $\{x_i\}_i$ where $x_0 = x_0$ and $x_{i+1} = T(x_i)$ and note that
$$
d(x_{i+1}, x_i) = d(T(x_{i}), T(x_{i-1})) \le q d(x_i, x_{i-1})
$$
but applying this repeatedly gives
$$
d(x_{i+1}, x_i) \le q^i d(x_1, x_0)
$$
or, that every point in the sequence get infinitely close together to its neighbor. In particular, we can prove that every point in the sequence, once far out enough, gets infinitely close to every other point in the sequence (that is, tell me a distance $\epsilon$ between any two points that you'd like, and I'll tell you some $N$ such that every $x_n$,  $n>N$ is always closer to every other such $x_{n'}$ for $n'>N$---in other words, go far out enough in the sequence and every point is always closer to each other point than any $\epsilon > 0$ you give me[^other]). This famous theorem is called Banach's fixed point theorem, which has applications anywhere from topology all the way to differential equations (it guarantees existence *and* uniqueness of solutions to some differential equations).

Knowing this, then, we can always guarantee the existence of a fixed point; actually, even better, we can *construct* that point! Just apply $T$ repeatedly until you're satisfied with the result. In the next post, we'll see that this guarantees the existence of fixed *sets* under several mappings $\{T_i\}_i$, which we'll call a fractal.

Pardon the long introduction, it's certainly not necessary to understand everything in this post to get a lot out of the latter one, but for those of you who enjoy getting some of the math background, I though this might be a good introduction to some aspects of topology. For a more complete one, which I highly recommend, read up (and do the exercises on!) Mendelson's *Introduction to Topology*. It's a great intro that requires nothing more than high-school level calculus (if that, even), but is by no means easy.



[^lp2]: This demans some explanation, sure. In particular, I'm referring to the space of functions $X$ such that $\int_\mathbb{R} dx\,|f(x)|^2 < \infty$ for $f \in X$. This is actually the space we commonly refer to in fields like quantum mechanics and such.

[^openness]: Using this definition, we should prove that an open ball is, indeed, open (it doesn't just immediatly follow from definition, but it's close). I leave that as an excercise to the reader.

[^contraction]: This is formally called a *contraction mapping*.

[^cauchy]: Mostly because this requires a reformulation of the definition of the limit into Cauchy sequences, but it's not too bad.

[^other]: And yet another way to picture this. If you give me the radius of an open ball, I can guarantee you that there is some point in the sequence such that, putting the ball around that point, guarantees that every other term in the sequence after it is inside of that ball.
