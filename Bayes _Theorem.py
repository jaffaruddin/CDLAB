# bayes theorem
def bayes_theorem(p_f, p_f_and_a):
  p_f_given_a = p_f_and_a / p_f
  return p_f_given_a
p_f = 0.2
p_f_and_a = 0.03
result = bayes_theorem(p_f, p_f_and_a)
print('p(A/F) = %.3f%%'%(result * 100))

-> p(A/F) = 15.000%
