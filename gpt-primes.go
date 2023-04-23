package main

import "fmt"

func main() {
	fmt.Println("Enter the limit up to which prime numbers are to be found: ")
	var limit int
	fmt.Scanln(&limit)

	primes := make([]bool, limit+1)
	for i := 2; i <= limit; i++ {
		primes[i] = true
	}

	for p := 2; p*p <= limit; p++ {
		if primes[p] {
			for i := p * p; i <= limit; i += p {
				primes[i] = false
			}
		}
	}

	fmt.Println("Prime numbers up to", limit, "are:")
	for p := 2; p <= limit; p++ {
		if primes[p] {
			fmt.Println(p)
		}
	}
}
