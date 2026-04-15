"use client";

import type { BikeDetailContentProps } from "./bike-detail-sheet.types";

export function BikeDetailSheetContent({
  bike,
  formattedReservedUntil,
}: BikeDetailContentProps) {
  return (
    <div className="px-4 text-sm text-muted-foreground">
      <p>
        <span className="font-medium text-foreground">
          Coordenadas:
        </span>{" "}
        {bike.latitude}, {bike.longitude}
      </p>
      {bike.reservedBy ? (
        <p className="mt-1">
          <span className="font-medium text-foreground">
            Reservada por:
          </span>{" "}
          {bike.reservedBy}
        </p>
      ) : null}
      {formattedReservedUntil && (
        <p className="mt-1">
          <span className="font-medium text-foreground">
            Reserva hasta:
          </span>{" "}
          {formattedReservedUntil}
        </p>
      )}
    </div>
  );
}


