import React, { Suspense } from 'react';
import { Canvas, useLoader } from '@react-three/fiber';
import { OBJLoader } from 'three/examples/jsm/loaders/OBJLoader';
import { MTLLoader } from 'three/examples/jsm/loaders/MTLLoader';

function Model() {
  const mtl = useLoader(MTLLoader, '/Logo3d/logo.mtl');
  const obj = useLoader(OBJLoader, '/Logo3d/logo.obj', (loader) => {
    mtl.preload();
    loader.setMaterials(mtl);
  });

  return <primitive object={obj} />;
}

function Logo() {
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

export default Logo;
