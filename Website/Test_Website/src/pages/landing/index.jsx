import React, { useState, useEffect } from 'react';
import { Link } from "react-router-dom";

import './styles.css';

function LandingPage() {
  const [timeLeft, setTimeLeft] = useState({
    days: 0,
    hours: 0,
    minutes: 0,
    seconds: 0
  });

  useEffect(() => {
    const countdownDate = new Date("2024-12-01T00:00:00").getTime(); // Target date

    const updateCountdown = () => {
      const now = new Date().getTime();
      const distance = countdownDate - now;

      if (distance < 0) {
        clearInterval(interval);
        return;
      }

      setTimeLeft({
        days: Math.floor(distance / (1000 * 60 * 60 * 24)),
        hours: Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60)),
        minutes: Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60)),
        seconds: Math.floor((distance % (1000 * 60)) / 1000)
      });
    };

    const interval = setInterval(updateCountdown, 1000);
    return () => clearInterval(interval); // Clear interval on component unmount
  }, []);

  return (
    <div className="landing-page">
      <header className="landing-header">
        <h1>Algothon 2024</h1>
      </header>

      <main>
        <section className="countdown">
          <h2>Get Coding!</h2>
          <div className="countdown-timer">
            <div className="countdown-item">
              <span className="countdown-number">{timeLeft.days}</span>
              <span className="countdown-label">Days</span>
            </div>
            <div className="countdown-item">
              <span className="countdown-number">{timeLeft.hours}</span>
              <span className="countdown-label">Hrs</span>
            </div>
            <div className="countdown-item">
              <span className="countdown-number">{timeLeft.minutes}</span>
              <span className="countdown-label">Mins</span>
            </div>
            <div className="countdown-item">
              <span className="countdown-number">{timeLeft.seconds}</span>
              <span className="countdown-label">Secs</span>
            </div>
          </div>
        </section>

        <section className="landing-buttons">
          <Link to="/submit" className="cta-btn">How to Submit</Link>
          <Link to="/info" className="cta-btn">Info Page</Link>
        </section>
      </main>

      <footer>
        <p>&copy; QuantSoc</p>
      </footer>
    </div>
  );
}

export default LandingPage;
