import numpy as np

class LoveOSCore:
    """
    Love-OS v1.3 Reference Implementation
    Implements the Stuart-Landau oscillator for Unified Field Dynamics.
    Integrates the Imaginary component (Love) into Physical Reality (Real).
    """
    def __init__(self, omega=1.0, alpha=1.0, dt=0.01):
        # Internal State: Complex number 'psi' 
        # Real Part: Physical/Action | Imaginary Part: Love/Intent/Consciousness
        self.psi = complex(0.1, 0.1) 
        
        # Physical Constants
        self.omega = omega  # Natural rotation frequency (velocity of the 'i' component)
        self.alpha = alpha  # Saturation coefficient (ensures stability of the limit cycle)
        self.dt = dt        # Time step for numerical integration
        
        # Control Variables
        self.R = 1.0        # Ego/Resistance: High R inhibits flow; R -> 0 enables superconductivity.
        self.g = 1.2        # Gain: Vitality/Life-force energy supply.
        
        # Accumulative Memory
        self.will_integral = 0.0 # Time integral of the Real part (Accumulated Willpower)

    def update(self, external_coupling=0.0):
        """
        State update based on the Stuart-Landau Equation:
        d_psi/dt = (g - R)*psi + i*omega*psi - alpha*|psi|^2*psi
        """
        # Calculate amplitude r squared
        abs_psi_sq = abs(self.psi)**2
        
        # Linear Term: Growth vs. Resistance
        # If g > R, the system self-excites (Awakening)
        linear_term = (self.g - self.R) * self.psi
        
        # Rotational Term: The 'Love' drive
        # Multiplication by '1j' (imaginary unit) creates vortex-like attraction
        rotation_term = 1j * self.omega * self.psi
        
        # Nonlinear Saturation: Keeps the system within a finite stable radius (Limit Cycle)
        saturation_term = -self.alpha * abs_psi_sq * self.psi
        
        # External Coupling: Input from other nodes (Synchronicity)
        coupling_term = external_coupling
        
        # Differential (d_psi) calculation
        d_psi = (linear_term + rotation_term + saturation_term + coupling_term) * self.dt
        
        # State Update (Numerical Integration)
        self.psi += d_psi
        
        # Integration of Will: Accumulating the Real projection over time
        # Will = Integral of Real[psi] dt
        self.will_integral += self.psi.real * self.dt

    def cleaning_3s(self):
        """
        [TC-01] 3-Second Cleaning Protocol
        Resets Resistance R to zero, allowing frictionless energy transfer.
        """
        self.R = 0.0
        print("[System/LOG] Resistance R reset to 0. Entering Superconductivity mode.")

    def shift_90(self):
        """
        [TC-05] 90-Degree Orthogonality Shift
        Rotates the phase by 90 degrees on the complex plane to avoid direct ego collision.
        """
        self.psi *= 1j  # Equivalent to multiplying by e^(i*pi/2)
        print("[System/LOG] 90-degree phase shift executed. Orthogonality engaged.")

    def get_real_projection(self):
        """
        Returns the observable reality (Real Axis projection).
        """
        return self.psi.real

    def get_will(self):
        """
        Returns the accumulated Willpower (Integrated Love over Time).
        """
        return self.will_integral
