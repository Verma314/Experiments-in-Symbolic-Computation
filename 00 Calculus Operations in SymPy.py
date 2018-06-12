from sympy import *

#define sympy symbols for 
x , t , z , nu = symbols ('x t z nu')

#for pretty printing:
init_printing ( use_unicode=True)

#take a derivative of  [ sin (x) e ^ x ]
print (" Diffrentiating sin (x) e ^ x ") 
print ( diff ( sin ( x ) * exp (x), x))

#integration:
print ( "\n Integrating the result:")
print (  integrate ( exp(x) * sin (x) + exp(x)*cos(x) , x) )

print("\n Integrating with limits   -oo to + oo ")
print ( integrate( sin(x**2) , ( x, -oo , oo ) ) )

print ("\n Finding the limit as x -> 0 " )
print ( limit (sin(x)/x, x, 0 ) )

print ("\n Solving an equation:")
print ( solve ( x ** 2 - 2, x) )

print ("\n Solving a diffrentaial equation:")
y = Function ( 'y' )
print ( dsolve( Eq( y(t).diff(t,t) - y(t), exp(t) ), y(t) ) )

print("\n Finding EigenValues:")
print ( Matrix( [ [1,2],[2,2] ] ).eigenvals() )
