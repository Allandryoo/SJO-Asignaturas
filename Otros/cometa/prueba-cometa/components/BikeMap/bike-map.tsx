"use client";

import { GoogleMap, Marker } from "@react-google-maps/api";
import { useCallback, useMemo, useState } from "react";

import { BikeDetailSheet } from "@/components/BikeDetailSheet";
import { useGoogleMaps } from "@/providers/google-maps-provider";
import {
    MAP_CONTAINER_STYLE,
    MAP_ZOOM,
    PALMA_CENTER,
} from "./bike-map.constants";
import { mapBikesToMarkers } from "./bike-map.mapper";
import { BikeMapProps } from "./bike-map.types";

export default function BikeMap({ bikes }: BikeMapProps) {
  const apiKey = process.env.NEXT_PUBLIC_GOOGLE_MAPS_API_KEY || "";
  const { isLoaded, loadError } = useGoogleMaps();

  const [selectedBikeId, setSelectedBikeId] = useState<number | null>(null);
  const [isSheetOpen, setIsSheetOpen] = useState(false);

  const markers = useMemo(() => mapBikesToMarkers(bikes), [bikes]);

  const selectedBike = useMemo(
    () => bikes.find((bike) => bike.id === selectedBikeId) ?? null,
    [bikes, selectedBikeId]
  );

  const handleMarkerClick = useCallback((bikeId: number) => {
    setSelectedBikeId(bikeId);
    setIsSheetOpen(true);
  }, []);

  const handleSheetOpenChange = useCallback((open: boolean) => {
    setIsSheetOpen(open);
    if (!open) {
      setSelectedBikeId(null);
    }
  }, []);

  if (loadError) {
    return (
      <div className="flex h-screen items-center justify-center">
        <div className="text-lg text-red-600">
          Error al cargar Google Maps: {loadError.message}
        </div>
      </div>
    );
  }

  if (!isLoaded) {
    return (
      <div className="flex h-screen items-center justify-center">
        <div className="text-lg">Cargando mapa...</div>
      </div>
    );
  }

  if (!apiKey) {
    return (
      <div className="flex h-screen items-center justify-center">
        <div className="text-lg text-red-600">
          Error: Google Maps API Key no configurada. Por favor, configura
          NEXT_PUBLIC_GOOGLE_MAPS_API_KEY en tu archivo .env
        </div>
      </div>
    );
  }

  return (
    <>
      <GoogleMap
        mapContainerStyle={MAP_CONTAINER_STYLE}
        center={PALMA_CENTER}
        zoom={MAP_ZOOM}
      >
        {markers.map((marker) => (
          <Marker
            key={marker.id}
            position={marker.position}
            title={marker.title}
            icon={marker.icon}
            onClick={() => handleMarkerClick(marker.id)}
          />
        ))}
      </GoogleMap>

      <BikeDetailSheet
        open={isSheetOpen}
        bike={selectedBike}
        handleOpenChange={handleSheetOpenChange}
      />
    </>
  );
}
