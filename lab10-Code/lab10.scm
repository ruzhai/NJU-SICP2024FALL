;;; Lab 10: Stream

;;; Required Problems

(define (filter-stream f s)
  (if (null? s)
      '() 
      
        (if (f (car s))
            (cons-stream (car s) (filter-stream f (cdr-stream s))) 
            (filter-stream f (cdr-stream s)))))


(define (slice s start end)
    (define (slice-helper s start end times)
        (cond 
             ((null? s) nil)
             
             ((= times end) nil)
             ((and (< times end) (>= times start)) (cons (car s) (slice-helper (cdr-stream s) start end (+ times 1))))
             (else
             (slice-helper (cdr-stream s) start end (+ times 1)))))
    (slice-helper s start end 0)
)


(define (naturals n)
  (cons-stream n (naturals (+ n 1))))


(define (combine-with f xs ys)
  (if (or (null? xs) (null? ys))
      nil
      (cons-stream
        (f (car xs) (car ys))
        (combine-with f (cdr-stream xs) (cdr-stream ys)))))


(define factorials
  (cons-stream 1 (combine-with * (naturals 1) factorials))
)


(define fibs
  (cons-stream 0 (cons-stream 1 (combine-with + fibs (cdr-stream fibs))))
  
)


(define (exp x)
  (define res (combine-with (lambda (i fact) (/ (expt x i) fact)) (naturals 0) factorials))
  (cons-stream 1(combine-with + (cdr-stream res) (exp x)))
  );敲重点



(define (list-to-stream lst)
  (if (null? lst) nil
      (cons-stream (car lst) (list-to-stream (cdr lst)))))



(define (nondecrease s)
  (define (group s current-group last-num)
    (cond
      ((null? s) 
       (if (null? current-group)
           '() 
           (cons-stream current-group '())))
      ((null? current-group)
       (group (cdr-stream s) (list (car s)) (car s)))
      ((>= (car s) last-num)  
       (group (cdr-stream s) (append current-group (list (car s))) (car s)))
      (else
       (cons-stream current-group (group (cdr-stream s) (list (car s)) (car s))))))

  (group s '() -999))



;;; Just For Fun Problems

(define (my-cons-stream first second) ; Does this line need to be changed?
  'YOUR-CODE-HERE
)

(define (my-car stream)
  'YOUR-CODE-HERE
)

(define (my-cdr-stream stream)
  'YOUR-CODE-HERE
)


(define (sieve s)
  'YOUR-CODE-HERE
)

(define primes (sieve (naturals 2)))
