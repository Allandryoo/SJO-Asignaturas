'use client';

import { useQuery } from '@tanstack/react-query';

interface Bike {
  id: number;
  status: 'AVAILABLE' | 'RESERVED' | 'IN_USE';
  latitude: string;
  longitude: string;
  reservedUntil: string | null;
  reservedBy: string | null;
  updatedAt: string;
  rideStartedAt: string | null;
}

interface BikesResponse {
  bikes: Bike[];
}

export function useBikes() {
  return useQuery<BikesResponse>({
    queryKey: ['bikes'],
    queryFn: async () => {
      const res = await fetch('/api/bikes');
      if (!res.ok) {
        throw new Error('Failed to fetch bikes');
      }
      return res.json();
    },
  });
}

