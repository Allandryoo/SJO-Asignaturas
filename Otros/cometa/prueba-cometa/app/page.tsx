'use client';

import BikeMap from '@/components/BikeMap';
import { useBikes } from '@/hooks/use-bikes';

export default function Home() {
  const { data, isLoading, error } = useBikes();

  if (isLoading) {
    return (
      <div className="flex items-center justify-center h-screen">
        <div className="text-lg">Cargando motos...</div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="flex items-center justify-center h-screen">
        <div className="text-lg text-red-600">
          Error al cargar las motos: {error.message}
        </div>
      </div>
    );
  }

  return (
    <div className="w-full h-screen">
      <BikeMap bikes={data?.bikes || []} />
    </div>
  );
}
