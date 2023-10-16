import React from 'react';

const VectaryEmbed: React.FC = () => {
  return (
    <div className="vectary-container">
      <iframe 
        src="https://app.vectary.com/p/2julLJnuAt1wyYfbJJkay2" 
        width="100%" 
        height="600" 
        allowFullScreen={true} 
        title="Vectary 3D Model"
        frameBorder={0}
        >
        </iframe>
    </div>
  );
}

export default VectaryEmbed;
