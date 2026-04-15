"use client";

import { SheetHeader, SheetDescription, SheetTitle } from "@/components/ui/sheet";
import type { BikeDetailHeaderProps } from "./bike-detail-sheet.types";
import type { Bike } from "@/components/BikeMap/bike-map.types";

function getStatusLabel(status: Bike["status"]) {
  switch (status) {
    case "AVAILABLE":
      return "Disponible";
    case "RESERVED":
      return "Reservada";
    case "IN_USE":
      return "En uso";
    default:
      return status;
  }
}

export function BikeDetailSheetHeader({ bike }: BikeDetailHeaderProps) {
  return (
    <SheetHeader>
      <SheetTitle>Moto #{bike.id}</SheetTitle>
      <SheetDescription>
        Estado actual:{" "}
        <span className="font-medium">
          {getStatusLabel(bike.status)}
        </span>
      </SheetDescription>
    </SheetHeader>
  );
}


