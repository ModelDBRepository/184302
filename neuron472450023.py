'''
Defines a class, Neuron472450023, of neurons from Allen Brain Institute's model 472450023

A demo is available by running:

    python -i mosinit.py
'''
class Neuron472450023:
    def __init__(self, name="Neuron472450023", x=0, y=0, z=0):
        '''Instantiate Neuron472450023.
        
        Parameters:
            x, y, z -- position offset
            
        Note: if name is not specified, Neuron472450023_instance is used instead
        '''
              
        self._name = name
        # load the morphology
        from load_swc import load_swc
        load_swc('Sst-IRES-Cre_Ai14_IVSCC_-165865.03.01.01_475332668_m.swc', self,
                 use_axon=False, xshift=x, yshift=y, zshift=z)

        # custom axon (works because dropping axon during import)
        from neuron import h
        self.axon = [h.Section(cell=self, name='axon[0]'),
                     h.Section(cell=self, name='axon[1]')]
        for sec in self.axon:
            sec.L = 30
            sec.diam = 1
            sec.nseg = 1
        self.axon[0].connect(self.soma[0](0.5))
        self.axon[1].connect(self.axon[0](1))
        self.all += self.axon
  
        self._insert_mechanisms()
        self._discretize_model()
        self._set_mechanism_parameters()
    
    def __str__(self):
        if self._name is not None:
            return self._name
        else:
            return "Neuron472450023_instance"
                
    def _insert_mechanisms(self):
        from neuron import h
        for sec in self.all:
            sec.insert("pas")
        for mech in [u'CaDynamics', u'Ca_HVA', u'Ca_LVA', u'Ih', u'Im_v2', u'K_T', u'Kd', u'Kv2like', u'Kv3_1', u'NaV', u'SK']:
            self.soma[0].insert(mech)
    
    def _set_mechanism_parameters(self):
        from neuron import h
        for sec in self.all:
            sec.Ra = 278.65
            sec.e_pas = -80.9754867554
        
        for sec in self.axon:
            sec.cm = 2.16
            sec.g_pas = 0.000296794714151
        for sec in self.dend:
            sec.cm = 2.16
            sec.g_pas = 2.28126091989e-05
        for sec in self.soma:
            sec.cm = 2.16
            sec.ena = 53.0
            sec.ek = -107.0
            sec.gbar_Ih = 0.0022078
            sec.gbar_NaV = 0.0809564
            sec.gbar_Kd = 0
            sec.gbar_Kv2like = 0.0074578
            sec.gbar_Kv3_1 = 0.0930522
            sec.gbar_K_T = 0.000316361
            sec.gbar_Im_v2 = 0.0060404
            sec.gbar_SK = 0.179155
            sec.gbar_Ca_HVA = 0.000862928
            sec.gbar_Ca_LVA = 0.00220059
            sec.gamma_CaDynamics = 1.16841e-05
            sec.decay_CaDynamics = 861.098
            sec.g_pas = 5.13923e-06
    
    def _discretize_model(self):
        for sec in self.all:
            sec.nseg = 1 + 2 * int(sec.L / 40)

