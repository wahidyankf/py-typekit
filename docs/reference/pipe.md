# `pipe`

Module `typekit.pipeline`, exported as `typekit.pipe`. It applies functions left to right.

## Signature

One overload per arity, from one function to nine:

```text
pipe[A, B](value: A, f1: Callable[[A], B], /) -> B
pipe[A, B, C](value: A, f1: Callable[[A], B], f2: Callable[[B], C], /) -> C
...
pipe[A, B, C, D, E, F, G, H, I, J](value: A, f1: Callable[[A], B], ..., f9: Callable[[I], J], /) -> J
```

## Behaviour

- `pipe(value, f1, f2)` is `f2(f1(value))`: each function runs exactly once, in argument order, on what the previous one
  returned, and the last result is returned.
- An exception a function raises propagates, and the later functions do not run.
- Each stage is typed from the one before, so a stage whose parameter does not accept the previous result is a Pyright
  error at that stage (`reportArgumentType`).
- More than nine functions: nest, as `pipe(pipe(value, f1, ..., f9), f10)`, which keeps every type.
- Pyright solves each stage from the input, so the input must carry its full type: a parameter, a function's return, or
  an unnarrowed annotation. A bare `Ok(2)` carries no error type: strict mode reports a lambda stage, whose parameter
  Pyright cannot infer, as partially unknown, and with a named function stage the result's error side stays an unsolved
  type variable that strict mode does not report.

The stages that make `pipe` chain a `Result` or an `Option` are the curried combinators of
[`typekit.result`](./result.md#curried-combinators) and [`typekit.option`](./option.md#curried-combinators).
