with open('index.html', 'r') as f:
    content = f.read()

OLD_START = '  <div class="cert-category">\n    <div class="cert-category-title">\n      <span class="cat-icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--gold)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/></svg></span>\n      <span class="cat-label">Research &amp; Academic Skills</span>'

pos = content.find(OLD_START)
end_pos = content.find('\n</section>', pos) + len('\n</section>')

NEW_CATS = '''  <div class="cert-category">
    <div class="cert-category-title">
      <span class="cat-icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--gold)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/></svg></span>
      <span class="cat-label">Research &amp; Academic Skills</span>
    </div>
    <div class="cert-grid">
      <div class="cert-card reveal" role="button" tabindex="0"><div class="cert-card-inner"><div class="cert-front"><div class="cert-front-top"><div class="cert-name">Academic Information Seeking</div><div class="cert-issuer">University of Copenhagen &amp; TU Denmark · Coursera</div></div><div class="cert-front-bottom"><span class="cert-year">2024</span><span class="cert-flip-hint">tap for details →</span></div></div><div class="cert-back"><div class="cert-back-title">Academic Information Seeking</div><div class="cert-back-issuer">University of Copenhagen &amp; Technical University of Denmark · Coursera</div><div class="cert-back-meta"><span class="cert-back-year">2024</span><a href="https://coursera.org/verify/NMTNPNAJUM2A" target="_blank" class="cert-verify">Verify Certificate ↗</a></div></div></div></div>
      <div class="cert-card reveal" role="button" tabindex="0"><div class="cert-card-inner"><div class="cert-front"><div class="cert-front-top"><div class="cert-name">Project: Writing a Research Paper</div><div class="cert-issuer">University of California, Irvine · Coursera</div></div><div class="cert-front-bottom"><span class="cert-year">2024</span><span class="cert-flip-hint">tap for details →</span></div></div><div class="cert-back"><div class="cert-back-title">Project: Writing a Research Paper</div><div class="cert-back-issuer">University of California, Irvine · Coursera</div><div class="cert-back-meta"><span class="cert-back-year">2024</span><a href="https://coursera.org/verify/PCHJDF3AJ2JG" target="_blank" class="cert-verify">Verify Certificate ↗</a></div></div></div></div>
      <div class="cert-card reveal" role="button" tabindex="0"><div class="cert-card-inner"><div class="cert-front"><div class="cert-front-top"><div class="cert-name">Research Design: Inquiry and Discovery</div><div class="cert-issuer">University of North Texas · Coursera</div></div><div class="cert-front-bottom"><span class="cert-year">2024</span><span class="cert-flip-hint">tap for details →</span></div></div><div class="cert-back"><div class="cert-back-title">Research Design: Inquiry and Discovery</div><div class="cert-back-issuer">University of North Texas · Coursera</div><div class="cert-back-meta"><span class="cert-back-year">2024</span><a href="https://coursera.org/verify/VVWLA3LMQ4GU" target="_blank" class="cert-verify">Verify Certificate ↗</a></div></div></div></div>
    </div>
  </div>

  <div class="cert-category">
    <div class="cert-category-title">
      <span class="cat-icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--gold)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M12 8v4"/><path d="M12 16h.01"/></svg></span>
      <span class="cat-label">Critical Thinking &amp; Problem Solving</span>
    </div>
    <div class="cert-grid">
      <div class="cert-card reveal" role="button" tabindex="0"><div class="cert-card-inner"><div class="cert-front"><div class="cert-front-top"><div class="cert-name">Solving Problems with Creative &amp; Critical Thinking</div><div class="cert-issuer">IBM · Coursera</div></div><div class="cert-front-bottom"><span class="cert-year">2023</span><span class="cert-flip-hint">tap for details →</span></div></div><div class="cert-back"><div class="cert-back-title">Solving Problems with Creative and Critical Thinking</div><div class="cert-back-issuer">IBM · Coursera</div><div class="cert-back-meta"><span class="cert-back-year">2023</span><a href="https://coursera.org/verify/EE44C7YWUJWD" target="_blank" class="cert-verify">Verify Certificate ↗</a></div></div></div></div>
      <div class="cert-card reveal" role="button" tabindex="0"><div class="cert-card-inner"><div class="cert-front"><div class="cert-front-top"><div class="cert-name">Mindware: Critical Thinking for the Information Age</div><div class="cert-issuer">University of Michigan · Coursera</div></div><div class="cert-front-bottom"><span class="cert-year">2024</span><span class="cert-flip-hint">tap for details →</span></div></div><div class="cert-back"><div class="cert-back-title">Mindware: Critical Thinking for the Information Age</div><div class="cert-back-issuer">University of Michigan · Coursera</div><div class="cert-back-meta"><span class="cert-back-year">2024</span><a href="https://coursera.org/verify/KMS9YEW9K6NC" target="_blank" class="cert-verify">Verify Certificate ↗</a></div></div></div></div>
      <div class="cert-card reveal" role="button" tabindex="0"><div class="cert-card-inner"><div class="cert-front"><div class="cert-front-top"><div class="cert-name">Welcome to Game Theory</div><div class="cert-issuer">The University of Tokyo · Coursera</div></div><div class="cert-front-bottom"><span class="cert-year">2024</span><span class="cert-flip-hint">tap for details →</span></div></div><div class="cert-back"><div class="cert-back-title">Welcome to Game Theory</div><div class="cert-back-issuer">The University of Tokyo · Coursera</div><div class="cert-back-meta"><span class="cert-back-year">2024</span><a href="https://coursera.org/verify/N4CHXJYFB5Q8" target="_blank" class="cert-verify">Verify Certificate ↗</a></div></div></div></div>
    </div>
  </div>

  <div class="cert-category">
    <div class="cert-category-title">
      <span class="cat-icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--gold)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20"/><path d="M2 12h20"/></svg></span>
      <span class="cat-label">Systems Thinking &amp; Sustainability</span>
    </div>
    <div class="cert-grid">
      <div class="cert-card reveal" role="button" tabindex="0"><div class="cert-card-inner"><div class="cert-front"><div class="cert-front-top"><div class="cert-name">Sustainability through Soccer: Systems-Thinking in Action</div><div class="cert-issuer">University of Virginia · Coursera</div></div><div class="cert-front-bottom"><span class="cert-year">2023</span><span class="cert-flip-hint">tap for details →</span></div></div><div class="cert-back"><div class="cert-back-title">Sustainability through Soccer: Systems-Thinking in Action</div><div class="cert-back-issuer">University of Virginia · Coursera</div><div class="cert-back-meta"><span class="cert-back-year">2023</span><a href="https://coursera.org/verify/PWG5G5XBYWLS" target="_blank" class="cert-verify">Verify Certificate ↗</a></div></div></div></div>
      <div class="cert-card reveal" role="button" tabindex="0"><div class="cert-card-inner"><div class="cert-front"><div class="cert-front-top"><div class="cert-name">Developing a Systems Mindset</div><div class="cert-issuer">University of Colorado Boulder · Coursera</div></div><div class="cert-front-bottom"><span class="cert-year">2023</span><span class="cert-flip-hint">tap for details →</span></div></div><div class="cert-back"><div class="cert-back-title">Developing a Systems Mindset</div><div class="cert-back-issuer">University of Colorado Boulder · Coursera</div><div class="cert-back-meta"><span class="cert-back-year">2023</span><a href="https://coursera.org/verify/SZ8SY9XEGD58" target="_blank" class="cert-verify">Verify Certificate ↗</a></div></div></div></div>
      <div class="cert-card reveal" role="button" tabindex="0"><div class="cert-card-inner"><div class="cert-front"><div class="cert-front-top"><div class="cert-name">Ecology: Ecosystem Dynamics and Conservation</div><div class="cert-issuer">American Museum of Natural History · Coursera</div></div><div class="cert-front-bottom"><span class="cert-year">2024</span><span class="cert-flip-hint">tap for details →</span></div></div><div class="cert-back"><div class="cert-back-title">Ecology: Ecosystem Dynamics and Conservation</div><div class="cert-back-issuer">American Museum of Natural History · Coursera</div><div class="cert-back-meta"><span class="cert-back-year">2024</span><a href="https://coursera.org/verify/8RXVJZNBGKQK" target="_blank" class="cert-verify">Verify Certificate ↗</a></div></div></div></div>
    </div>
  </div>

  <div class="cert-category">
    <div class="cert-category-title">
      <span class="cat-icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--gold)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M22 10v6M2 10l10-5 10 5-10 5z"/><path d="M6 12v5c3 3 9 3 12 0v-5"/></svg></span>
      <span class="cat-label">Education &amp; Community Engagement</span>
    </div>
    <div class="cert-grid">
      <div class="cert-card reveal" role="button" tabindex="0"><div class="cert-card-inner"><div class="cert-front"><div class="cert-front-top"><div class="cert-name">What Future for Education?</div><div class="cert-issuer">University of London &amp; UCL · Coursera</div></div><div class="cert-front-bottom"><span class="cert-year">2023</span><span class="cert-flip-hint">tap for details →</span></div></div><div class="cert-back"><div class="cert-back-title">What Future for Education?</div><div class="cert-back-issuer">University of London &amp; UCL Institute of Education · Coursera</div><div class="cert-back-meta"><span class="cert-back-year">2023</span><a href="https://coursera.org/verify/34UBAA4PVD36" target="_blank" class="cert-verify">Verify Certificate ↗</a></div></div></div></div>
      <div class="cert-card reveal" role="button" tabindex="0"><div class="cert-card-inner"><div class="cert-front"><div class="cert-front-top"><div class="cert-name">Strategies for Effective Engagement</div><div class="cert-issuer">University of Colorado Boulder · Coursera</div></div><div class="cert-front-bottom"><span class="cert-year">2023</span><span class="cert-flip-hint">tap for details →</span></div></div><div class="cert-back"><div class="cert-back-title">Strategies for Effective Engagement</div><div class="cert-back-issuer">University of Colorado Boulder · Coursera</div><div class="cert-back-meta"><span class="cert-back-year">2023</span><a href="https://coursera.org/verify/455Q9FTTB4WA" target="_blank" class="cert-verify">Verify Certificate ↗</a></div></div></div></div>
    </div>
  </div>

  <div class="cert-category">
    <div class="cert-category-title">
      <span class="cat-icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--gold)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg></span>
      <span class="cat-label">Futures &amp; Foresight</span>
    </div>
    <div class="cert-grid">
      <div class="cert-card reveal" role="button" tabindex="0"><div class="cert-card-inner"><div class="cert-front"><div class="cert-front-top"><div class="cert-name">Ready, Set, Future! Introduction to Futures Thinking</div><div class="cert-issuer">Institute for the Future · Coursera</div></div><div class="cert-front-bottom"><span class="cert-year">2023</span><span class="cert-flip-hint">tap for details →</span></div></div><div class="cert-back"><div class="cert-back-title">Ready, Set, Future! Introduction to Futures Thinking</div><div class="cert-back-issuer">Institute for the Future · Coursera</div><div class="cert-back-meta"><span class="cert-back-year">2023</span><a href="https://coursera.org/verify/3JHVF3DX54QB" target="_blank" class="cert-verify">Verify Certificate ↗</a></div></div></div></div>
    </div>
  </div>

  <div class="cert-category">
    <div class="cert-category-title">
      <span class="cat-icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--gold)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="23 6 13.5 15.5 8.5 10.5 1 18"/><polyline points="17 6 23 6 23 12"/></svg></span>
      <span class="cat-label">Entrepreneurship &amp; Innovation</span>
    </div>
    <div class="cert-grid">
      <div class="cert-card reveal" role="button" tabindex="0"><div class="cert-card-inner"><div class="cert-front"><div class="cert-front-top"><div class="cert-name">Building Fintech Startups in Emerging Markets</div><div class="cert-issuer">University of Cape Town · Coursera</div></div><div class="cert-front-bottom"><span class="cert-year">2023</span><span class="cert-flip-hint">tap for details →</span></div></div><div class="cert-back"><div class="cert-back-title">Building Fintech Startups in Emerging Markets</div><div class="cert-back-issuer">University of Cape Town · Coursera</div><div class="cert-back-meta"><span class="cert-back-year">2023</span><a href="https://coursera.org/verify/2CRA4NT6SEBM" target="_blank" class="cert-verify">Verify Certificate ↗</a></div></div></div></div>
      <div class="cert-card reveal" role="button" tabindex="0"><div class="cert-card-inner"><div class="cert-front"><div class="cert-front-top"><div class="cert-name">New Product Development for Start-Ups</div><div class="cert-issuer">Coursera Project Network</div></div><div class="cert-front-bottom"><span class="cert-year">2023</span><span class="cert-flip-hint">tap for details →</span></div></div><div class="cert-back"><div class="cert-back-title">New Product Development for Small Businesses and Start-Ups</div><div class="cert-back-issuer">Coursera Project Network</div><div class="cert-back-meta"><span class="cert-back-year">2023</span><a href="https://coursera.org/verify/JVNTSPGK8Q4V" target="_blank" class="cert-verify">Verify Certificate ↗</a></div></div></div></div>
      <div class="cert-card reveal" role="button" tabindex="0"><div class="cert-card-inner"><div class="cert-front"><div class="cert-front-top"><div class="cert-name">Innovation Through Design: Think, Make, Break, Repeat</div><div class="cert-issuer">University of Sydney · Coursera</div></div><div class="cert-front-bottom"><span class="cert-year">2023</span><span class="cert-flip-hint">tap for details →</span></div></div><div class="cert-back"><div class="cert-back-title">Innovation Through Design: Think, Make, Break, Repeat</div><div class="cert-back-issuer">University of Sydney · Coursera</div><div class="cert-back-meta"><span class="cert-back-year">2023</span><a href="https://coursera.org/verify/RSQSVV2356M6" target="_blank" class="cert-verify">Verify Certificate ↗</a></div></div></div></div>
      <div class="cert-card reveal" role="button" tabindex="0"><div class="cert-card-inner"><div class="cert-front"><div class="cert-front-top"><div class="cert-name">Beyond Silicon Valley: Entrepreneurship in Transitioning Economies</div><div class="cert-issuer">Case Western Reserve University · Coursera</div></div><div class="cert-front-bottom"><span class="cert-year">2024</span><span class="cert-flip-hint">tap for details →</span></div></div><div class="cert-back"><div class="cert-back-title">Beyond Silicon Valley: Growing Entrepreneurship in Transitioning Economies</div><div class="cert-back-issuer">Case Western Reserve University · Coursera</div><div class="cert-back-meta"><span class="cert-back-year">2024</span><a href="https://coursera.org/verify/XMETXE5UMTUR" target="_blank" class="cert-verify">Verify Certificate ↗</a></div></div></div></div>
      <div class="cert-card reveal" role="button" tabindex="0"><div class="cert-card-inner"><div class="cert-front"><div class="cert-front-top"><div class="cert-name">Strategic Career Self-Management</div><div class="cert-issuer">State University of New York · Coursera</div></div><div class="cert-front-bottom"><span class="cert-year">2024</span><span class="cert-flip-hint">tap for details →</span></div></div><div class="cert-back"><div class="cert-back-title">Strategic Career Self-Management</div><div class="cert-back-issuer">State University of New York · Coursera</div><div class="cert-back-meta"><span class="cert-back-year">2024</span><a href="https://coursera.org/verify/S85U3R7L5F69" target="_blank" class="cert-verify">Verify Certificate ↗</a></div></div></div></div>
    </div>
  </div>

  <div class="cert-category">
    <div class="cert-category-title">
      <span class="cat-icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--gold)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg></span>
      <span class="cat-label">Diversity, Equity &amp; Inclusion</span>
    </div>
    <div class="cert-grid">
      <div class="cert-card reveal" role="button" tabindex="0"><div class="cert-card-inner"><div class="cert-front"><div class="cert-front-top"><div class="cert-name">Gender Analytics for Innovation</div><div class="cert-issuer">University of Toronto · Coursera</div></div><div class="cert-front-bottom"><span class="cert-year">2023</span><span class="cert-flip-hint">tap for details →</span></div></div><div class="cert-back"><div class="cert-back-title">Gender Analytics for Innovation</div><div class="cert-back-issuer">University of Toronto · Coursera</div><div class="cert-back-meta"><span class="cert-back-year">2023</span><a href="https://coursera.org/verify/A4VSDZJC8CWD" target="_blank" class="cert-verify">Verify Certificate ↗</a></div></div></div></div>
      <div class="cert-card reveal" role="button" tabindex="0"><div class="cert-card-inner"><div class="cert-front"><div class="cert-front-top"><div class="cert-name">Queering Identities: LGBTQ+ Sexuality and Gender Identity</div><div class="cert-issuer">University of Colorado System · Coursera</div></div><div class="cert-front-bottom"><span class="cert-year">2023</span><span class="cert-flip-hint">tap for details →</span></div></div><div class="cert-back"><div class="cert-back-title">Queering Identities: LGBTQ+ Sexuality and Gender Identity</div><div class="cert-back-issuer">University of Colorado System · Coursera</div><div class="cert-back-meta"><span class="cert-back-year">2023</span><a href="https://coursera.org/verify/FXDNA5Y97PWW" target="_blank" class="cert-verify">Verify Certificate ↗</a></div></div></div></div>
    </div>
  </div>

  <div class="cert-category">
    <div class="cert-category-title">
      <span class="cat-icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--gold)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="6"/><path d="M15.477 12.89L17 22l-5-3-5 3 1.523-9.11"/></svg></span>
      <span class="cat-label">Leadership &amp; Global Recognition</span>
    </div>
    <div class="cert-grid">
      <div class="cert-card reveal" role="button" tabindex="0"><div class="cert-card-inner"><div class="cert-front"><div class="cert-front-top"><div class="cert-name">Millennium Fellowship Project Certificate</div><div class="cert-issuer">UN Academic Impact &amp; MCN</div></div><div class="cert-front-bottom"><span class="cert-year">2023</span><span class="cert-flip-hint">tap for details →</span></div></div><div class="cert-back"><div class="cert-back-title">Millennium Fellowship Project Certificate — Africa Jobs SL</div><div class="cert-back-issuer">United Nations Academic Impact &amp; Millennium Campus Network · Signed by Robert Skinner (UN) &amp; Sam Vaghar (MCN)</div><div class="cert-back-meta"><span class="cert-back-year">2023 · UN · MCN</span></div></div></div></div>
    </div>
  </div>

</section>'''

new_content = content[:pos] + NEW_CATS
# Append everything after the old </section>
new_content += content[end_pos:]

with open('index.html', 'w') as f:
    f.write(new_content)

print('Done. New length:', len(new_content))
