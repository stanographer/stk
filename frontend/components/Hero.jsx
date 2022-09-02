import React from 'react';

import Logo from './Logo';

const Hero = () => (
  <div className="hero my-5 text-center" data-testid="hero">
    <Logo testId="hero-logo" />
    <h1 className="mb-4" data-testid="hero-title">
     STK (Styktin)rstrs so fptstds
    </h1>

    <p className="lead" data-testid="hero-lead">
      Manage, export, and sync your steno dictionaries in one place.{' '}
      <a href="https://nextjs.org">Next.js</a>
    </p>
  </div>
);

export default Hero;
