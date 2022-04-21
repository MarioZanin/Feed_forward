# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 23:52:25 2022

@author: MarioCelso
"""

from linear_algebra import dot
import math

def sigmoid(t):
    return 1 / (1 + math.exp(-t))

def neuron_output(weights, inputs):
    return sigmoid(dot(weights, inputs))

def feed_forward(neural_network, input_vector):
    """recebe uma rede neural (representada como uma lista de pesos) e retorna a saida
    da programação direta da entrada"""
    
    outputs = []
    
    for layer in neural_network:
        
        input_with_bias = input_vector + [1]              # add a bias input
        output = [neuron_output(neuron, input_with_bias)  # compute the output
                  for neuron in layer]                    # for this layer
        outputs.append(output)                            # and remember it
        
        # the input to the next layer is the output of this one
        input_vector = output
        
    return outputs

xor_network = [# camada oculta
               [[20, 20, -30],   # neurônio AND
                [20, 20, -10]],  # neurônio OR
               # output layer
               [[-60, 60, -30]]] # meurônio = segunda entrada
                                # menos a primeira entrada
                                
for x in [0, 1]:
    for y in [0, 1]:
        print (x, " EXCLUSIVO ", y, " = ", feed_forward(xor_network, [x,y])[-1])
        