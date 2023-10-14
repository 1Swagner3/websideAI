import React from 'react';
import { Canvas } from '@react-three/fiber';
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';

function Model() {
  const model = useLoader(GLTFLoader, '../public/Logo3d/logo3d.gltf');

  return <primitive object={model.scene} />;
}

function Logo() {
  return (
    <Canvas>
      <ambientLight />
      <pointLight position={[10, 10, 10]} />
      <Model />
    </Canvas>
  );
}

export default Logo;
