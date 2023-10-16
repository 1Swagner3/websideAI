import React, { Suspense } from 'react';
import { Canvas, useLoader } from '@react-three/fiber';
import { GLTFLoader } from 'three/examples/jsm/loaders/GLTFLoader';

function Model() {
  const glb = useLoader(GLTFLoader, '/Logo3d/logo_animation.glb');

  return <primitive object={glb.scene} scale={[10, 10, 10]}/>;
}

const Logo_GLB: React.FC = () => {
  return (
    <Canvas>
      <ambientLight />
      <pointLight position={[10, 10, 10]} />
      <Suspense fallback={null}>
        <Model />
      </Suspense>
    </Canvas>
  );
}

export default Logo_GLB;
