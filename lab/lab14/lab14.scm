(define (split-at lst n)
  (cond ((null? lst) (cons nil nil))
        ((equal? n 0) (cons nil lst))
        (else
        (cons (cons (car lst) (car (split-at (cdr lst) (- n 1)))
        ) (cdr (split-at (cdr lst) (- n 1))))))
)

'another way to do it
'((let result (split-at (cdr lst) (- n 1)))
  (cons (cons (car lst) (car result)) (cdr result)))


(define (compose-all funcs)
  (if (null? funcs) (lambda (x) x)
      (lambda (x) ((compose-all (cdr funcs)) ((car funcs) x)) ))
)

