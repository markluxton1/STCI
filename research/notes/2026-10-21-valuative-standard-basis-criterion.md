# Valuative standard-basis test — working note

At p in smooth C, let B=k[[t]], R=B[[x,y]], J=(F,G), with F,G a regular sequence and C=(x,y) contained in V(J). Generic transverse length m=length_{k((t))[[x,y]]} k((t))[[x,y]]/J_eta. Special length λ_p=length_{k[[x,y]]} k[[x,y]]/(J+(t)), possibly infinite.

If V(J) has no residual curve through p, its support is C locally. Then A=R/J is finite over B and CM of dimension one, hence finite free of rank m and λ_p=m. Conversely, if a residual curve passes through p, λ_p>m (or infinite), by intersection positivity / conservation of number. A finite special colength allows Weierstrass/finite projection and the rank counts generic branches. For each field separately a local standard basis of J_eta and J_p yields monomial initial ideals whose colengths are m and λ_p. Generic basis cannot merely be specialized without tracking vanishing leading coefficients.

Test example: F=x², G=x²+t y³+y⁴. Generic local ideal (x²,y³) length 6, special (x²,y⁴) length 8. Residual curve x=0,t+y=0 contributes 2. Weighted initial forms and cancellation G-F=y³(t+y) detect this.

Important caveat: ordinary tropicalization of a zero-dimensional scheme supported at the origin in the torus is empty; a tropical basis of supports alone does not recover length. Use local standard bases, weighted initial ideals with multiplicity, or tropical schemes. Global STCI equality de=4m implies λ_p=m for every p; this is a necessary local test, not yet a novel numerical exclusion.

Status: provisional research note, not independently audited.
