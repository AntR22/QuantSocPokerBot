import React, { useState } from 'react';
import './styles.css';

function Info() {
  const [openItem, setOpenItem] = useState(null);

  const toggleAnswer = (index) => {
    setOpenItem(openItem === index ? null : index);
  };

  return (
    <div className="container">
      <header>
        <h1>Comp - Information</h1>
      </header>

      <main>
        <section className="intro">
          <h2>About the Event</h2>
          <p>
            Info
          </p>
        </section>

        <section className="faq">
          <h2>Frequently Asked Questions (FAQ)</h2>

          <div className="faq-item">
            <button className="question" onClick={() => toggleAnswer(1)}>
              What is this competition about?
            </button>
            <div className="answer" style={{ display: openItem === 1 ? 'block' : 'none' }}>
              <p>Placeholder Text</p>
            </div>
          </div>

          <div className="faq-item">
            <button className="question" onClick={() => toggleAnswer(2)}>
              Who can participate?
            </button>
            <div className="answer" style={{ display: openItem === 2 ? 'block' : 'none' }}>
              <p>Placeholder Text</p>
            </div>
          </div>
        </section>
      </main>

      <footer>
        <p>&copy; QuantSoc</p>
      </footer>
    </div>
  );
}

export default Info;
