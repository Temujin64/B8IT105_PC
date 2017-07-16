#1 Function for the addition calculation.	
addit <- function(first, second)
	first + second
	
addit(8,7)

#2 Function for the subtraction calculation.	
subit <- function(first, second)
  first - second

subit(8,7)

#3 Function for the multiplication calculation.	
multit <- function(first, second)
  first * second

multit(8,7)

#4 Function for the division calculation.
divit <- function(first, second)
  first / second
  
divit(8,7)

#5 Function for the exponentiation calculation.		
expit <- function(first, second)
  first ** second

expit(8,7)

factit <- function(n)
  if (n > 1) {
    n * factit(n - 1)
}
  if (n < 0) {
     print('inf')
}
  1

#6 Function for the factorisation calculation.	
factit <- function(n) {
  if      (n == 0)    return (1)
  else if (n < 0)     return ('Infinity')
  else           return (n * factit(n-1))
  }

factit(-1)
factit(0)
factit(6)


#7 Function for the combinations rule calculation.
combit <- function(n, r)
  factit(n)/(factit(r)*factit(n-r))

combit(6,4)


#8 Function for the average calculation.
avit <- function(data) {
  sumdata <- sum(data)
  n <- length(data)
   sumdata / n
 }

avit(c(10.0, 11.0, 13.0, 12.0, 10.0, 11.0, 14.0, 9.0))

#9 Function for the variance calculation.
varit <- function(v, sample) {
  m = avit(v)
  n <- length(v)
  pop <- avit((m - v)^2)
  if (sample == FALSE) {pop}
  else if (sample == TRUE) {pop * n/(n-1)}
}

varit(c(10, 11, 13, 12, 10, 11, 14, 9), TRUE)
varit(c(10, 11, 13, 12, 10, 11, 14, 9), FALSE)


#10 Function for the standard deviation calculation.
sdev <- function(v, sample) {
  m = avit(v)
  n <- length(v)
  pop <- avit((m - v)^2)
  if (sample == FALSE) {sqrt(pop)}
  else if (sample == TRUE) {sqrt(pop * n/(n-1))}
}

sdev(c(10, 11, 13, 12, 10, 11, 14, 9), TRUE)
sdev(c(10, 11, 13, 12, 10, 11, 14, 9), FALSE)