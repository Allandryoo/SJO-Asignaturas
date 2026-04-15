export interface Bike {
  id: number;
  status: 'AVAILABLE' | 'RESERVED' | 'IN_USE';
  latitude: string;
  longitude: string;
  reservedUntil: string | null;
  reservedBy: string | null;
}

export interface BikeMapProps {
  bikes: Bike[];
}

export interface BikeMarker {
  id: number;
  position: {
    lat: number;
    lng: number;
  };
  status: Bike['status'];
  title: string;
  icon: string;
}

