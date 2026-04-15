import { Bike, BikeMarker } from './bike-map.types';

/**
 * Obtiene el color del icono según el estado de la moto
 */
function getStatusColor(status: Bike['status']): string {
  switch (status) {
    case 'AVAILABLE':
      return '#22c55e'; // Verde
    case 'RESERVED':
      return '#eab308'; // Amarillo
    case 'IN_USE':
      return '#ef4444'; // Rojo
    default:
      return '#3b82f6'; // Azul
  }
}

/**
 * Crea un SVG personalizado con el icono de moto de Lucide y color según el estado
 */
function createMotorbikeIconSVG(color: string): string {
  const svg = `
    <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="${color}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <circle cx="12" cy="12" r="11" fill="white" stroke="${color}" stroke-width="2"/>
      <path d="m18 14-1-3"/>
      <path d="m3 9 6 2a2 2 0 0 1 2-2h2a2 2 0 0 1 1.99 1.81"/>
      <path d="M8 17h3a1 1 0 0 0 1-1 6 6 0 0 1 6-6 1 1 0 0 0 1-1v-.75A5 5 0 0 0 17 5"/>
      <circle cx="19" cy="17" r="3" fill="${color}"/>
      <circle cx="5" cy="17" r="3" fill="${color}"/>
    </svg>
  `;
  // Convertir SVG a data URL para que Google Maps lo acepte
  return `data:image/svg+xml;charset=utf-8,${encodeURIComponent(svg.trim())}`;
}

/**
 * Obtiene el icono del marker según el estado de la moto
 */
export function getMarkerIcon(status: Bike['status']): string {
  const color = getStatusColor(status);
  return createMotorbikeIconSVG(color);
}

/**
 * Convierte una lista de motos en markers para Google Maps
 */
export function mapBikesToMarkers(bikes: Bike[]): BikeMarker[] {
  return bikes.map((bike) => ({
    id: bike.id,
    position: {
      lat: parseFloat(bike.latitude),
      lng: parseFloat(bike.longitude),
    },
    status: bike.status,
    title: `Moto #${bike.id} - ${bike.status}`,
    icon: getMarkerIcon(bike.status),
  }));
}

